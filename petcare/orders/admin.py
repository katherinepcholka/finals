from django.contrib import admin

from .models import Order, OrderItem

@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    fields = [ "order", "product", "price", "quantity", "status" ]
    list_display = ("order", "quantity", "product", "price", "status" )
    list_display_links = ("product", )
    ordering = ["status", "-id"]
    list_editable = ("status", )
    search_fields = ["product__name", "order__first_name"]
    list_filter = ["order__first_name", "status"]


@admin.register(Order)
class RecipientAdmin(admin.ModelAdmin):
    fields = [ "first_name", "email", "phone" ]
    list_display = ("first_name", "email", "phone")
    list_display_links = ("first_name", )
    ordering = ["first_name", "-id"]