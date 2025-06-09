from django.contrib import admin

from .models import Flat, Report, Owner


class FlatsInstanceInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner',]


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ['created_at', ]
    list_display = ['address', 'price', 'new_building', 'construction_year', ]
    list_editable = ['new_building', ]
    list_filter = ['new_building', 'rooms_number', 'has_balcony', ]
    raw_id_fields = ['liked_by', ]
    inlines = [FlatsInstanceInline]


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'apartment_complainer',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats', ]