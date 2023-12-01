from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'quantity_available')
    search_fields = ('name', 'category__name')  # добавлен поиск по категории

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'text', 'rating')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'cart', 'quantity')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'shipping_address', 'date_ordered', 'is_paid')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity')
   

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)   
