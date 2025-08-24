from django.db import models
from home.models import *


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category/')
    about_kitchen = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "دسته ها"
        verbose_name = "وعده"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='menu/')
    active = models.BooleanField(default=True, null=True, blank=True)

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(r.value for r in ratings) / ratings.count(), 1)
        return 0


class Rating(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="ratings")
    value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.fullname
