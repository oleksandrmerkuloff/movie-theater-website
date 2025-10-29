from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'total_text', 'status']
    list_filter = ['created_at', 'status']
    sortable_by = ['total_text', 'status']
    ordering = ['-created_at']


admin.site.register(Order, OrderAdmin)
