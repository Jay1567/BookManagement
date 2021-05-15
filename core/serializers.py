from rest_framework import serializers
from .models import Category, Author, Book

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'categoryName']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id' ,'authorName']


class BookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    author = serializers.SerializerMethodField('get_author')

    def get_category(self, book):
        try:
            bookCategory = Category.objects.filter(book=book.ISBN)
            return CategorySerializer(bookCategory, many=True).data
        except Category.DoesNotExist:
            return None

    def get_author(self, book):
        try:
            bookAuthor = Author.objects.filter(book=book.ISBN)
            return AuthorSerializer(bookAuthor, many=True).data
        except Author.DoesNotExist:
            return None

    def create(self, validated_data):
        print(validated_data)
        categories = validated_data.pop('category')
        authors = validated_data.pop('author')

        book = Book.objects.create(**validated_data)
        if authors:
            for author in authors:
                check = Author.objects.get(authorName=author)
                if check is None:
                    check = Author.objects.create(authorName=author)
                book.author.add(check)

        if categories:
            for category in categories:
                check = Category.objects.get(authorName=category)
                if check is None:
                    check = Category.objects.create(authorName=category)
                book.category.add(check)


        return book


    class Meta:
        model = Book
        fields = ['ISBN' ,'bookName', 'category', 'author']