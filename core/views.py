from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from core.forms import BookingForm, BrandForm, ContactForm, SubscriberForm, TestimonialForm
from .models import About, Brand, Car, Carousel, Testimonial
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def home(request):
    items = Car.objects.all()
    carousel_product_1 = Carousel.objects.all()[0] if Carousel.objects.all().count() > 0 else Carousel.objects.all()
    carousel_product_2 = Carousel.objects.all()[1] if Carousel.objects.all().count() > 0 else Carousel.objects.all()
    carousel_product_3 = Carousel.objects.all()[2] if Carousel.objects.all().count() > 0 else Carousel.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        'items': items,
        'carousel_product_1': carousel_product_1,
        'carousel_product_2': carousel_product_2,
        'carousel_product_3': carousel_product_3,
        'testimonial': testimonial,
    }
    return render(request, 'index.html', context)


def service(request):
    cars = Car.objects.all()
    p = Paginator(cars, 2)
    page = request.GET.get('page')
    car_pages = p.get_page(page)

    context = {
        'cars': car_pages,
    }
    return render(request, 'service.html', context)


@login_required
def car_details_view(request, slug):
    template_name = 'car_details.html'
    details = get_object_or_404(Car, slug=slug)
    context = {
        'details': details,
        'link': 'cars'
        # 'main_specs':main_specs,
    }
    return render(request, template_name, context)


def about(request):
    template_name = 'about.html'
    abouts = About.objects.all()
    context = {
        'abouts': abouts
    }
    return render(request, template_name, context)


def contact(request):
    template_name = 'contact.html'
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            form.send()
            messages.success(request, 'You have successfully Contacted FastCars Organization.')
            return redirect('core:contact')
        else:
            messages.error(request, 'Invalid Submission , failed')

    context = {
        'contact': form,
        'link': 'contact'
    }
    return render(request, template_name, context)


def search(request):
    template_name = 'search.html'
    user_search = request.GET.get("search")
    # cars = Car.objects.order_by('created_date')
    if user_search:
        cars = Car.objects.filter(Q(car_name__icontains=user_search))
    else:
        cars = Car.objects.all()

    p = Paginator(cars, 2)
    page = request.GET.get('page')
    car_pages = p.get_page(page)

    context = {
        'cars': cars,
        'car_pages': car_pages,
    }
    return render(request, template_name, context)


def product_brand(request, slug):
    template_name = "brand_category.html"
    cars = Car.objects.all()
    brand = get_object_or_404(Brand, slug=slug)
    car = Car.objects.filter(brand__slug=slug)
    p = Paginator(cars, 2)
    page = request.GET.get('page')
    car_pages = p.get_page(page)
    context = {
        'cars': cars,
        'brand': brand,
        "car": car,
        'car_pages': car_pages,
    }
    return render(request, template_name, context)


def brand(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands
    }
    return render(request, 'brand.html', context)


@login_required
def create_brand(request):
    if request.method == 'POST':
        brand = request.POST['brand']
        if brand:
            brand = Brand(brand=brand)
            brand.save()
            return redirect('core:brand')
    context = {

    }
    return render(request, 'brand.html', context)


@login_required
def brand_update(request, id):
    brand = get_object_or_404(Brand, id=id)
    form = BrandForm(request.POST or None, instance=brand)
    if request.method == 'POST':
        form = BrandForm(request.POST or None, instance=brand)
        if form.is_valid():
            form.save()
            brand_update = f'You have update {brand.brand} brand'
            messages.success(request, brand_update)
            return redirect('core:brand')
        else:
            form = BrandForm(request.POST)

    context = {
        'brand': brand,
        'form': form
    }
    return render(request, 'brand_update.html', context)


@login_required
def delete_brand(request, id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    return redirect('core:brand')


def booking_view(request, slug):
    template_name = 'booking.html'
    car = get_object_or_404(Car, slug=slug)
    form = BookingForm()
    if request.POST:
        form = BookingForm(request.POST or None)
        if form.is_valid():
            c = form.save(commit=False)
            c.user = request.user
            c.car = car
            c.save()
            messages.success(request, 'You have successfully booked the car')
            return redirect('core:home')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    context = {
        'form': form,
        'car': car
    }
    return render(request, template_name, context)


def testimonials(request):
    template_name = 'post-testimonials.html'
    form = TestimonialForm()
    if request.POST:
        form = TestimonialForm(request.POST or None, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial Posted Successfully')
            return redirect('core:home')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    context = {
        'post_testimonials': form,
    }
    return render(request, template_name, context)


# def subscriber(request):
#     template_name = 'footer.html'
#     subform = SubscriberForm()
#     if request.POST:
#         subform = SubscriberForm(request.POST or None)
#         if subform.is_valid():
#             subform.save()
#             return redirect('/')
#         else:
#             messages.error(request, 'Invalid Submission ,Request failed')
#     context = {
#         'subform': subform,
#     }
#     return render(request, template_name, context)
