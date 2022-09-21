# from service.models import *
# from .models import *
# from django.db.models import Q


# def product_renderer(request):
#     brand = Brand.objects.all()
#     counts = []
#     for c in brand:
#         brand_count = Car.objects.filter(brand=c).count()
#         counts.append(brand_count)

#     brand_count = zip(brand, counts)
#     return {
#         'brand': brand,
#         'brand_count': brand_count,
#         'counts': counts,
#     }
