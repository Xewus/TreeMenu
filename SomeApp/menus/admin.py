from django.contrib import admin

from .models import MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    verbose_name = 'Подменю'
    verbose_name_plural = 'Подменю'
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('level', 'name', 'url')
    ordering = ('level', 'name')
    list_filter = ('level', 'name')
    search_fields = ('name',)
    fields = ('name', 'parent')
    inlines = (MenuItemInline,)
