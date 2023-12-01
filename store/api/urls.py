# api/urls.py
from django.urls import path
from .views import (
    CategoryList, CategoryDetail, ProductList, ProductDetail,
    ReviewList, ReviewDetail, CartList, CartDetail,
    OrderList, OrderDetail, ProductSearchView, OrderHistoryView
)

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list-create'),  # создает POST / отображает GET
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'), # достать категорию GET, обновить PATCH, удалить DELETE
    path('products/', ProductList.as_view(), name='product-list-create'), # отображать GET / создать POST
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'), # достать продукт GET / обновить PATCH / удалить DELETE
    path('reviews/', ReviewList.as_view(), name='review-list'), # достать обзор GET / создать POST
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('carts/', CartList.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('orders/history/', OrderHistoryView.as_view(), name='order-history'),
]
