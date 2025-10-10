from django.contrib import admin

from cart.models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ['product', 'quantity']
    readonly_fields = ['id',]
    autocomplete_fields = ['product',]


class CartAdmin(admin.ModelAdmin):
    fields = ['user',]
    readonly_fields = ['id', 'created_at', 'total']
    ordering = ['-created_at']
    list_display = ['user', 'created_at', 'total']
    autocomplete_fields = ['user']
    list_per_page = 50
    list_filter = ['created_at',]
    inlines = [CartItemInline,]


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem)
