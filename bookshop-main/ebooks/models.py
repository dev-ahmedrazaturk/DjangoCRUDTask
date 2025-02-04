from django.db import models
from django.template.defaultfilters import title, length


# Create your models here.

class MyBook(models.Model):  # Use PascalCase for class names
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    genre = models.CharField(max_length=64)
    stock = models.IntegerField()

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, "
                f"Price: {self.price}, Genre: {self.genre}")
