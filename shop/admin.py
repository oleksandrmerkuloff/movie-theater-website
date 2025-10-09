from django.contrib import admin

from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'in_stock', 'price', 'image']
    list_display = ['name', 'in_stock', 'price']
    list_editable = ['in_stock']
    readonly_fields = ['added_at', 'id']
    search_fields = ['name', 'price']
    list_filter = ['in_stock', '-added_at', 'price']
    list_per_page = 30


admin.site.register(Product, ProductAdmin)
