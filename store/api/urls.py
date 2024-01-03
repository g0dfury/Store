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

    path('carts/', CartCreate.as_view(), name='cart-list'), # пустая корзина
    path('carts/<int:cart_id>/add/', CartList.as_view(), name='add-to-cart'), # заполнение корзины

    path('users/profile/', UserProfileView.as_view(), name='user-profile'), # изменение информации, удаление и получение только для авторизированного пользователя
    
    path('admin/products/', ProductAdminListCreateView.as_view(), name='product-admin-list-create'), # создать посмотреть продукты (для админа)
    path('admin/products/<int:pk>/', ProductAdminDetailView.as_view(), name='product-admin-detail'), # обновить удалить получить по id (для админа)
    path('admin/users/delete/<int:pk>/', UserAdminDeleteView.as_view(), name='user-admin-delete'), # удалить профиль (для админа)

    path('orders/create/', OrderCreate.as_view(), name='order-create'),
    path('orders/history/', OrderHistory.as_view(), name='order-history'),
]

