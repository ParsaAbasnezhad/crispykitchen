from django.contrib import admin
from .models import Food, DiningTable, Reservation, ReservationItem



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "slug")
    list_filter = ("price",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("slug",)



@admin.register(DiningTable)
class DiningTableAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "location", "is_active")
    list_filter = ("is_active", "location")
    search_fields = ("name", "location")



class ReservationItemInline(admin.TabularInline):
    model = ReservationItem
    extra = 1



@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("customer_name", "customer_phone", "table", "start_time", "end_time", "service_type", "paid")
    list_filter = ("service_type", "paid", "start_time")
    search_fields = ("customer_name", "customer_phone", "customer_email")
    inlines = [ReservationItemInline]
    readonly_fields = ("created_at",)