from rest_framework import serializers
from .models import Category, Post, Comment


class CategoryListSerializer(serializers.ModelSerializer):
    """Category (list)"""

    class Meta:
        model = Category
        exclude = ['description', 'order']


class PostListSerializer(serializers.ModelSerializer):
    """Post (list)"""

    class Meta:
        model = Post
        exclude = ['description', 'body', 'order', 'offer_url', 'public', 'update']


class CategoryDetailSerializer(serializers.ModelSerializer):
    """Category (detail)"""
    posts = PostListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class Comment