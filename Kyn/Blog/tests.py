from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Blog, Entry
from .serializers import BlogSerializer, EntrySerializer

class BlogAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.blog1 = Blog.objects.create(name='Blog 1', tagline='Tagline 1')
        self.blog2 = Blog.objects.create(name='Blog 2', tagline='Tagline 2')

    def test_get_all_blogs(self):
        url = reverse('blog-list-create')
        response = self.client.get(url)
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_get_single_blog(self):
        url = reverse('blog-retrieve-update-destroy', args=[self.blog1.pk])
        response = self.client.get(url)
        blog = Blog.objects.get(pk=self.blog1.pk)
        serializer = BlogSerializer(blog)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    # Add more test cases as needed for create, update, delete operations

class EntryAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.blog = Blog.objects.create(name='Blog', tagline='Tagline')
        self.entry1 = Entry.objects.create(blog=self.blog, headline='Headline 1', body_text='Body text 1', pub_date='2023-01-01')
        self.entry2 = Entry.objects.create(blog=self.blog, headline='Headline 2', body_text='Body text 2', pub_date='2023-01-02')

    def test_get_all_entries(self):
        url = reverse('entry-list-create')
        response = self.client.get(url)
        entries = Entry.objects.all()
        serializer = EntrySerializer(entries, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    def test_get_single_entry(self):
        url = reverse('entry-retrieve-update-destroy', args=[self.entry1.pk])
        response = self.client.get(url)
        entry = Entry.objects.get(pk=self.entry1.pk)
        serializer = EntrySerializer(entry)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), serializer.data)

    # Add more test cases as needed for create, update, delete operations
