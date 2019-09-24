from . import views
from django.urls import path


urlpatterns = [
   path('',views.PostListView.as_view(template_name='blog/home.html'),name='blog-list'),
   path('post-new',views.PostCreateView.as_view(),name='post-new'),
   path('post/<str:slug>/',views.PostDetailView,name='post-detail'),
   path('post/<str:slug>/update',views.PostUpdateView.as_view(),name='post-update'),
   path('post/<str:slug>/delete',views.PostDeleteView.as_view(),name='post-delete'),
   path('user/<str:username>',views.UserPostListView.as_view(template_name = 'blog/user_posts.html'),name='user-posts'),
   path('category/<str:name>',views.CategoryPostListView.as_view(template_name='blog/home.html'),name='category-posts'),
   path('myposts/<str:username>',views.MyPosts.as_view(template_name='blog/myposts.html'),name='myposts-posts'),
   path('post/<str:slug>/addwatchlist',views.PostAddToWatchListToggle.as_view(),name='post-addwl'),
   path('watchlist/',views.WatchList.as_view(template_name='blog/wishlist.html'),name='wishlist'),
   path('comments/<int:id>/delete',views.comment_delete,name='delete'),

   
  
]