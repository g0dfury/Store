from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'quantity_available')
    search_fields = ('name', 'category__name')  # добавлен поиск по категории
    list_filter = ('id', 'category', 'price', ) # фильтрация товаров

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id','cart', 'quantity', 'product')
    list_filter = ('cart', )

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'shipping_address', 'date_ordered', 'is_paid')
    
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(Cart, CartAdmin)
# admin.site.register(CartItem, CartItemAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart)
admin.site.register(CartItems)
admin.site.register(Orders)
admin.site.register(OrderedItems)