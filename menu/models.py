from django.db import models
from home.models import *



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category/')
    about_kitchen = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    views = models.IntegerField()
    score = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu/')


    def __str__(self):
        return self.name


class Comment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.fullname
