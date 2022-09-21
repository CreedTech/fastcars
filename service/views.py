# from pyexpat.errors import messages
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Car, Brand
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# # from .forms import BrandForm, BookingForm
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required


# def service(request):
#     cars = Car.objects.all()
#     p = Paginator(cars, 2)
#     page = request.GET.get('page')
#     car_pages = p.get_page(page)

#     context = {
#         'cars': car_pages,
#     }
#     return render(request, 'service.html', context)
