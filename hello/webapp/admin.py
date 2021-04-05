from django.contrib import admin
from webapp.models import Product, Basket


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'remainder', 'price']
    list_filter = ['category']
    fields = ['name', 'description', 'category', 'remainder', 'price']


class BaskedAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'amount']


admin.site.register(Product, ProductsAdmin)
admin.site.register(Basket, BaskedAdmin)
# Register your models here.
