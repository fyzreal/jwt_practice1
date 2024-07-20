from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Book(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    fathers_name = models.CharField(max_length=50)