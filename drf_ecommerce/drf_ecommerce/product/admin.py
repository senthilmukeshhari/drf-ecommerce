from django.contrib import admin
from drf_ecommerce.product.models import Category, Product, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
