from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import BlogPost
from Kyn.Blog.models import Author


class BlogPostTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='John Doe', email='johndoe@example.com')
        self.blog_post = BlogPost.objects.create(title='Test Blog Post', content='This is a test blog post.', pub_date='2022-01-01', author=self.author)

    def test_get_blog_post_list(self):
        url = reverse('blog-post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results', [])), 1)
        self.assertEqual(response.json().get('results', [])[0].get('title'), 'Test Blog Post')

    def test_get_blog_post_detail(self):
        url = reverse('blog-post-detail', args=[self.blog_post.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), 'Test Blog Post')

    # Add more test cases as needed

    def test_create_blog_post(self):
        url = reverse('blog-post-list')
        data = {
            'title': 'New Blog Post',
            'content': 'This is a new blog post.',
            'pub_date': '2022-02-01',
            'author': self.author.pk
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)
        self.assertEqual(BlogPost.objects.last(), 'New Blog Post')

    # Add more test cases for update, delete, etc.
