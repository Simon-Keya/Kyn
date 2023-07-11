from django.urls import path
from .views import BlogListCreateAPIView, BlogRetrieveUpdateDestroyAPIView, EntryListCreateAPIView, EntryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('blogs/', BlogListCreateAPIView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(), name='blog-retrieve-update-destroy'),
    path('entries/', EntryListCreateAPIView.as_view(), name='entry-list-create'),
    path('entries/<int:pk>/', EntryRetrieveUpdateDestroyAPIView.as_view(), name='entry-retrieve-update-destroy'),
]
