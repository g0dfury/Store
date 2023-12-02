# api/urls.py
from django.urls import path
from .views import (
    CategoryList, CategoryDetail, ProductList, ProductDetail,
    ReviewList, ReviewDetail, CartList, CartDetail,
    OrderList, OrderDetail, ProductSearchView, OrderHistoryView, 
    ProductByCategoryList
)

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list-create'),  # создает POST / отображает GET
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'), # достать категорию GET, обновить PATCH, удалить DELETE
    path('categories/<int:category_id>/products/', ProductByCategoryList.as_view(), name='products-by-category'), # возвращает товары по категории
    
    path('products/', ProductList.as_view(), name='product-list-create'), # отображать GET / создать POST
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'), # достать продукт GET / обновить PATCH / удалить DELETE
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    
    path('reviews/', ReviewList.as_view(), name='review-list'), # -
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'), # -
    
    path('carts/', CartList.as_view(), name='cart-list'), # -
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart-detail'), # -
    
    path('orders/', OrderList.as_view(), name='order-list'), # - 
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'), # -
    path('orders/history/', OrderHistoryView.as_view(), name='order-history'), # -

]
