from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.utils import timezone


class Food(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='foods/', blank=True, null=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class DiningTable(models.Model):
    name = models.CharField(max_length=50, help_text="مثل: میز 1، VIP-2")
    capacity = models.PositiveIntegerField(default=2)
    location = models.CharField(max_length=80, blank=True, help_text="داخل سالن، تراس و ...")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]
        unique_together = ("name", "location")

    def __str__(self):
        return f"{self.name} (ظرفیت {self.capacity})"



class Reservation(models.Model):
    DELIVERY_CHOICES = (
        ("dine_in", "صرف در رستوران"),
        ("take_away", "بیرون‌بر"),
    )

    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    customer_email = models.EmailField(blank=True)
    table = models.ForeignKey(DiningTable, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name="reservations")


    start_time = models.DateTimeField()
    end_time = models.DateTimeField(help_text="مثلاً 1 یا 2 ساعت بعد از شروع")


    service_type = models.CharField(max_length=20, choices=DELIVERY_CHOICES, default="dine_in")
    address = models.TextField(blank=True, help_text="برای بیرون‌بر (اختیاری)")
    note = models.TextField(blank=True)

    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_time"]
        indexes = [
            models.Index(fields=["start_time", "end_time"]),
        ]

    def clean(self):

        if self.end_time <= self.start_time:
            raise ValidationError("زمان پایان باید بعد از زمان شروع باشد.")

        if self.table_id:
            overlap = Reservation.objects.filter(
                table_id=self.table_id,
                start_time__lt=self.end_time,
                end_time__gt=self.start_time,
            ).exclude(pk=self.pk).exists()
            if overlap:
                raise ValidationError("برای این بازه زمانی، این میز قبلاً رزرو شده است.")


        if self.service_type == "take_away" and not self.address:
            raise ValidationError("برای بیرون‌بر، آدرس الزامی است.")

    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        base = f"رزرو {self.customer_name} - {timezone.localtime(self.start_time).strftime('%Y-%m-%d %H:%M')}"
        return f"{base} ({'با میز ' + self.table.name if self.table else 'بدون میز'})"


class ReservationItem(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="items")
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("reservation", "food")

    def subtotal(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.food.name} × {self.quantity}"
