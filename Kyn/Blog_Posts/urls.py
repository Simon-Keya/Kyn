from django.urls import path
from .views import BlogPostList, BlogPostDetail

urlpatterns = [
    path('', BlogPostList.as_view(), name='blog-post-list'),
    path('<int:pk>/', BlogPostDetail.as_view(), name='blog-post-detail'),
]
