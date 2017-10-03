from django.contrib import admin

from .models import Charge


class ChargeAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'charge_date',
        'value',
        'is_paid',
        'period',
        'is_active',
    )

    list_filter = ('is_paid', 'is_active', 'charge_date', 'value', 'title',)


admin.site.register(Charge, ChargeAdmin)
