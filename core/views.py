from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer
from .models import Category, Author, Book

class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer