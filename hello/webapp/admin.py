from django.contrib import admin
from webapp.models import Product, Basket, Order, IntermediateTable


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'remainder', 'price']
    list_filter = ['category']
    fields = ['name', 'description', 'category', 'remainder', 'price']


class BaskedAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'amount']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'phone_number', 'address']
    list_filter = ['user_name']


class IntermediateTableAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'order', 'amount']


admin.site.register(Product, ProductsAdmin)
admin.site.register(Basket, BaskedAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(IntermediateTable, IntermediateTableAdmin)

# Register your models here.
