from django.contrib import admin
from .models import About, Brand, Car, Booking, Carousel, ContactDetail, ContactInfo, Subscriber, Testimonial
# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'booking_date', 'To_agree',)
    search_fields = ('booking_date',)
    list_editable = ('To_agree',)


admin.site.register(About)
admin.site.register(Carousel)
admin.site.register(ContactDetail)
admin.site.register(ContactInfo)
admin.site.register(Subscriber)
admin.site.register(Testimonial)
