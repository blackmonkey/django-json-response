from django.db import models

__all__ = ['Author', 'Book', 'Publisher']


class Publisher(models.Model):
  name = models.CharField(max_length=100)


class Author(models.Model):
  name = models.CharField(max_length=100)


class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
  publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
