from django import template
from blog.models import Category,Post
import random
register=template.Library()

@register.inclusion_tag("blog/category_list.html")
def category_list():
    categories=Category.objects.all()
    return {'categories': categories}

@register.inclusion_tag("blog/last_added.html")
def last_addedposts():
    posts_last2=Post.objects.filter(draft = False).order_by('-modified_on')[:2]
    return {"posts_last2":posts_last2}

@register.inclusion_tag("blog/random_post.html")
def random_post():
    count = Post.objects.count()
    random_object = Post.objects.all()[random.randint(0,count-1)]
    if random_object:
        return {"random_obj" : random_object }


@register.inclusion_tag("blog/popular_post.html")
def popular_post():

    popular_post =  Post.objects.filter(draft = False).order_by('-read_count').first()       
    return {"popular_post" : popular_post}