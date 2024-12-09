from django.contrib import admin
from .models import Product,ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'price_per_unit', 'description')
    search_fields = ('name',)
    list_filter = ('unit',)
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
