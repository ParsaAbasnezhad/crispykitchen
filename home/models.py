from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class CategoryEvent(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category_events/', null=True, blank=True)


class CategoryNewsletter(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()



class TeamMember(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='team_members/')
    responsibility = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    email = models.EmailField(null=True, blank=True)


class Newsletter(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='newsletters/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(CategoryNewsletter, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='events/')
    category = models.ForeignKey(CategoryEvent, on_delete=models.CASCADE)
