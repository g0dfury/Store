from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list-create'),  # создает POST / отображает GET
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'), # достать категорию GET, обновить PATCH, удалить DELETE
    path('categories/<int:category_id>/products/', ProductByCategoryList.as_view(), name='products-by-category'), # возвращает товары по категории
    
    path('products/', ProductList.as_view(), name='product-list-create'), # список продуктов
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'), # конкретный продукт
    path('products/search/', ProductSearchView.as_view(), name='product-search'), # поиск продукта

    path('users/profile/', UserProfileView.as_view(), name='user-profile'), # 
    
    path('admin/products/', ProductAdminCreateView.as_view(), name='product-admin-create'), # создать товар (админ только)
    path('admin/products/<int:pk>/', ProductAdminDetailView.as_view(), name='product-admin-detail'), # редактирование товара (админ)
    path('admin/users/delete/<int:pk>/', UserAdminDeleteView.as_view(), name='user-admin-delete'), # удаление пользователя (админ)
    path('admin/categories/create/', CategoryCreate.as_view(), name = 'category-create' ),
    path('admin/categories/edit/<int:pk>/', CategoryEdit.as_view(), name = 'category-edit'),

    path('carts/', CartView.as_view()),
    path('order/', OrderAPI.as_view())
]

