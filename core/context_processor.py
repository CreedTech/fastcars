from django.shortcuts import redirect
from core.forms import SubscriberForm
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def product_renderer(request):
    brand = Brand.objects.all()
    contact_info = ContactInfo.objects.all()
    p = Paginator(brand, 2)
    page = request.GET.get('page')
    car_pages = p.get_page(page)
    counts = []
    for c in brand:
        brand_count = Car.objects.filter(brand=c).count()
        counts.append(brand_count)

    brand_count = zip(brand, counts)

    subform = SubscriberForm()
    if request.POST:
        subform = SubscriberForm(request.POST or None)
        if subform.is_valid():
            subform.save()
            subform.send()
            messages.success(request, 'You have Successfully Subscribed.')
        else:
            messages.error(request, 'Invalid Submission ,Request failed')
    return {
        'brand': brand,
        'brand_count': brand_count,
        'contact_info': contact_info,
        'counts': counts,
        'car_pages': car_pages,
        'subform': subform,
    }
