from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=40)
    born_location = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.fullname



class Quote(models.Model):
    tags = ArrayField(models.CharField(max_length=30), max_length=10)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.CharField(max_length=250, null=False)
