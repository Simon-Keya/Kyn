from rest_framework import serializers
from .models import Blog, Author, Entry


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class EntrySerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Entry
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    entries = EntrySerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'
