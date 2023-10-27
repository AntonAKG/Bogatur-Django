from django.contrib import admin

from .models import User, Coach, Ticket


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'type_day', 'price',)


class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'descriptions', 'price_per_training')



admin.site.register(User)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Ticket, TicketAdmin)
