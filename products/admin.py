from django.contrib import admin
from products.models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock')
    list_filter = ('price', 'stock')
    search_fields = ('name', 'description') 