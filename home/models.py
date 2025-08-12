from django.contrib.auth.models import AbstractUser
from django.db import models


class CategoryEvent(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category_events/', null=True, blank=True)


class CategoryNewsletter(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='team_members/')
    responsibility = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    email = models.EmailField(null=True, blank=True)


class Newsletter(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)
    image = models.ImageField(upload_to='newsletters/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(CategoryNewsletter, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)


class Event(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='events/')
    category = models.ForeignKey(CategoryEvent, on_delete=models.CASCADE)
