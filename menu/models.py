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
    name = models.CharField(max_length=100,verbose_name='غذا')
    original_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="قیمت اصلی")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,verbose_name="قیمت با تخفیف")
    views = models.IntegerField(verbose_name="بازدید")
    score = models.FloatField(default=0,verbose_name="امتیاز")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="وعده")
    image = models.ImageField(upload_to='menu/',verbose_name="عکس غذا")
    active = models.BooleanField(default=True,null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(default=timezone.now, null=True, blank=True)


    def __str__(self):
        return self.fullname
