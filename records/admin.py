from django.contrib import admin
from .models import Records, Category  # Corrected import


class RecordsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'display_categories',
        'releasedate',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

    def display_categories(self, obj):
        """Create a string for the Category. This is required to display ManyToManyField in list_display."""
        return ', '.join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Categories'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Records, RecordsAdmin)
admin.site.register(Category, CategoryAdmin)
