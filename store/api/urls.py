# api/urls.py
from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list-create'),  # создает POST / отображает GET
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'), # достать категорию GET, обновить PATCH, удалить DELETE
    path('categories/<int:category_id>/products/', ProductByCategoryList.as_view(), name='products-by-category'), # возвращает товары по категории
    
    path('products/', ProductList.as_view(), name='product-list-create'), # отображать GET / создать POST
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'), # достать продукт GET / обновить PATCH / удалить DELETE
    path('products/search/', ProductSearchView.as_view(), name='product-search'), # поиск товаров через query = value

    path('carts/', CartCreate.as_view(), name='cart-list'), # -
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart-detail'), # -
    path('carts/<int:cart_id>/add/', CartList.as_view(), name='add-to-cart'),
]
