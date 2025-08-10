from django.contrib import admin
from .models import TeamMember, CategoryNewsletter, Newsletter

admin.site.register(Newsletter)
admin.site.register(CategoryNewsletter)
admin.site.register(TeamMember)
