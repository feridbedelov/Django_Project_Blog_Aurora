from django.shortcuts import render,get_object_or_404,HttpResponseRedirect

from .models import Post,Category
from comments.models import Comment
from comments.forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,RedirectView
from django .contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .utils import get_read_time
from django.db.models import F


class PostAddToWatchListToggle(RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        slug=self.kwargs.get("slug")
        obj = get_object_or_404(Post, slug=slug)
        url_ = '/watchlist/'
        user = self.request.user
        
        if user.is_authenticated:
            if user in obj.watchlist.all():
                obj.watchlist.remove(user)
            else:
                obj.watchlist.add(user)
            
       
        return url_

class WatchList(LoginRequiredMixin,ListView):
    model=Post
    paginate_by=5

    def get_queryset(self):
        userq=self.request.user
        return Post.objects.filter(watchlist=userq).order_by('-created_at') 



class PostListView(ListView):
    model=Post
    paginate_by= 5

    def get_queryset(self):
        return Post.objects.filter(draft=False).order_by('-created_at')

class UserPostListView(ListView):
    model=Post
    paginate_by= 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user,draft=False).order_by('-created_at')

class CategoryPostListView(ListView):
    model=Post
    paginate_by= 5

    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs.get('name'))
        return Post.objects.filter(category=category,draft=False).order_by('-created_at')

class MyPosts(LoginRequiredMixin,ListView):
    model =Post
    paginate_by=5
    context_object_name = 'posts'

    def get_queryset(self):
        user=self.request.user
        return Post.objects.filter(author=user).order_by('-created_at')




# class PostDetailView(DetailView):
#     model=Post


def PostDetailView(request,slug):
    obj = get_object_or_404(Post,slug = slug)
    if not obj.draft:
        obj.read_count  = obj.read_count + 1 
        obj.save()

    
    comments = obj.comments
    
    initial_data ={
        "content_type":obj.get_content_type,
        "object_id" : obj.id
    }

    form = CommentForm(request.POST or None,initial=initial_data)
    if form.is_valid():
        c_type=form.cleaned_data.get("content_type")
        content_type=ContentType.objects.get(model=c_type)
        obj_id= form.cleaned_data.get("object_id")
        content=form.cleaned_data.get("content")
        parent_obj = None

        try:
            parent_id= int(request.POST.get('parent_id'))
        except:
            parent_id=None
        if parent_id:
            qs = Comment.objects.filter(id=parent_id)
            if qs.exists() and qs.count()==1:
                parent_obj=qs.first()


        new_comment = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id=obj_id,
            content=content,
            parent=parent_obj
        )
        return HttpResponseRedirect(obj.get_absolute_url())


    context ={
        "object":obj,
        "comments":comments,
        "comment_form":form

    }
    return render(request,'blog/post_detail.html',context)


def comment_delete(request,id):
    obj = Comment.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(obj.content_object.get_absolute_url())

    





class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content','category','rating','image','draft']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content','category','rating','image','draft']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False






