from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = [ "name", "category", "is_available" ]
    prepopulated_fields = {"slug": ("name",)}
    list_display = ( "category", "name", "is_available"  )
    list_display_links = ("name", )
    ordering = ["category", "-id"]
    list_editable = ("is_available", )
    search_fields = ["name", "category__name"]
    list_filter = ["category__name", "is_available"]


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)

