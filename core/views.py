from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CategorySerializer, AuthorSerializer, BookSerializer
from .models import Category, Author, Book

# class CategoryView(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        # print(request)
        # print(request.data)
        serializer = BookSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)