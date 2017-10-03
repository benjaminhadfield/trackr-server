from django.contrib import admin

from .models import Charge


class ChargeAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'charge_date',
        'value',
        'title',
        'is_paid',
        'is_active',
    )

    list_filter = ('is_paid', 'charge_date',)


admin.site.register(Charge, ChargeAdmin)
