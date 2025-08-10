from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    message = models.TextField()
    date_time = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.full_name} | {self.phone}'


class Weekday(models.Model):
    day_open = models.CharField(max_length=20)
    time_open = models.CharField(max_length=20)
    day_close = models.CharField(max_length=20)
    time_close = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.day_open} | {self.time_open} | {self.day_close} | {self.time_close}'
