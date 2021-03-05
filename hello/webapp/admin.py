from django.contrib import admin
from webapp.models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'remainder', 'price']
    list_filter = ['category']
    fields = ['category', 'description', 'category', 'remainder', 'price']


admin.site.register(Product, ProductsAdmin)
# Register your models here.
