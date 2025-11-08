from django.contrib import admin

from .models import Hall, Session, Seat


class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows', 'seats_per_row')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'start_time', 'price_standard')
    list_filter = ('hall', 'start_time')


class SeatAdmin(admin.ModelAdmin):
    list_display = ('session', 'row', 'seat', 'is_booked', 'is_premium')
    list_filter = ('is_booked', 'is_premium')


admin.site.register(Session, SessionAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Seat, SeatAdmin)
