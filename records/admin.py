from django.contrib import admin
from .models import Records, Category

# Register your models here.

class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Records, RecordAdmin)
admin.site.register(Category, CategoryAdmin)