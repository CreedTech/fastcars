from django.urls import path

from .views import (
    about,
    booking_view,
    brand,
    brand_update,
    car_details_view,
    create_brand,
    delete_brand,
    home,
    contact,
    search,
    product_brand,
    service,
    testimonials,
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('car-details/<str:slug>', car_details_view, name='car-details'),
    path('booking/<slug>/', booking_view, name='booking'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('post-testimonials', testimonials, name='post-testimonials'),
    path('brand', brand, name='brand'),
    path('create_brand', create_brand, name='create_brand'),
    path('brand_update/<int:id>', brand_update, name='brand_update'),
    path('delete_brand/<int:id>', delete_brand, name='delete_brand'),
    path('product/brand/<str:slug>', product_brand, name='product_brand'),
]
