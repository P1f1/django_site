from django.contrib import admin
from .models import Product, Review, Manufacturer, Profile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'desc', 'image', 'price', 'stock', 'status', 'manufacturer']
    list_filter = ['status', 'price', 'manufacturer']
    search_fields = ['name', 'desc']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['status', 'price', 'name', 'manufacturer']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'product', 'text', 'created']
    list_filter = ['created', 'updated']
    search_fields = ['name', 'text']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name', ]
    search_fields = ['name', ]
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
