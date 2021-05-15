from rest_framework import serializers
from .models import Category, Author, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'categoryName')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id' ,'authorName')


class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.RelatedField(source='Category', read_only=True)
    author_name = serializers.RelatedField(source='Author', read_only=True)

    class Meta:
        model = Book
        fields = ('ISBN' ,'bookName', 'category_name', 'author_name')