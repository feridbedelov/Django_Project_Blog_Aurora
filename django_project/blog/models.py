from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db.models import Q
from PIL import Image
from django.db.models.signals import pre_save
from django.utils.text import slugify
from comments.models import Comment
from .utils import get_read_time



class BlogPostQuerySet(models.QuerySet):

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query)|
                    Q(author__username__icontains=query) 
                    )

        return self.filter(lookup,draft=False)



class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    
    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)






class Category(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to="post_pics",null=True,blank=True,
                            width_field="width_field",
                            height_field="height_field"     
                            )
    height_field = models.IntegerField(default=0,null=True,blank=True)
    width_field = models.IntegerField(default=0,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_on=models.DateTimeField(auto_now=True)
    draft=models.BooleanField(default=True)
    rating=models.FloatField(default=0,
                            null=True,
                            blank=True,
                            validators=[MinValueValidator(0.0),MaxValueValidator(10.0)]
                            )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)
    watchlist=models.ManyToManyField(User,blank=True,null=True,related_name="posts_watchlist")
    slug=models.SlugField(unique=True )
    read_time = models.IntegerField(default=0)
    read_count =  models.PositiveIntegerField(default= 0)
     


    objects=BlogPostManager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'slug':self.slug})
    
    def get_watchlist_url(self):
        return reverse('post-addwl',kwargs={'slug':self.slug})
    

    @property
    def comments(self):
        instance = self
        return Comment.objects.filter_by_instance(instance)
    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type
    

def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=Post.objects.filter(slug=slug).order_by("-id")
    exists= qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug



def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)
    
    if instance.content:
        sentence = instance.content
        read_time=get_read_time(sentence)
        instance.read_time=read_time

pre_save.connect(pre_save_post_receiver,sender=Post)



    



