# admin.py
from django.contrib import admin
from .models import Product, RealEstate, Vehicle, Category, SubCategory, Offer

admin.site.register(Product)
admin.site.register(RealEstate)
admin.site.register(Vehicle)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Offer)
