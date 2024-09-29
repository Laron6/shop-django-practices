from django.db import models

from django.db import models


# Модель Author
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# Модель Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель Book
class Book(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Связь один ко многим с Author
    publisher = models.ManyToManyField(Publisher)  # Связь многие ко многим с Publisher

    def __str__(self):
        return self.title
