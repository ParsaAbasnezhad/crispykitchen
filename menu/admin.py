from django.contrib import admin
from menu.models import *

admin.site.register(Rating)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'original_price', 'image')
    search_fields = ('name',)
    list_filter = ('active',)
