from django.db import models


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


class Newsletter(models.Model):
    email = models.EmailField()
    title = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='newsletters/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(CategoryNewsletter, on_delete=models.CASCADE, null=True, blank=True)


