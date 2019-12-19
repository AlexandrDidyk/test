from django.contrib import admin

from .models import Table, Order


class OrderInline(admin.StackedInline):
    model = Order


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'seats', 'shape', 'position_x', 'position_y',
        'length', 'width'
    )
    list_filter = ('shape', )
    search_fields = ('number', )
    ordering = ('number',)
    inlines = [
        OrderInline
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'table', 'email')
    list_filter = ('table', )
    search_fields = ('email', )
    ordering = ('date',)
