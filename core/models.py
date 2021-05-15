from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length=70, unique=True)
    
    class Meta:
        db_table = 'Category'

    def __str__(self):
        return self.categoryName


class Author(models.Model):
    authorName = models.CharField(max_length=100, null=False, unique=True)
    
    class Meta:
        db_table = 'Author'

    def __str__(self):
        return self.authorName



class Book(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True)
    bookName = models.CharField(max_length=250, null=False)
    category = models.ManyToManyField(Category, verbose_name="category", db_column='category')
    author = models.ManyToManyField(Author, verbose_name="Author", db_column='author')

    class Meta:
        db_table = 'Book'

    def __str__(self):
        return self.bookName