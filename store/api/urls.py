from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),  # list categories 
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-retrieve'), # get category
    path('categories/<int:category_id>/products/', ProductByCategoryList.as_view(), name='products-by-category'), # sort by category
    
    path('products/', ProductList.as_view(), name='product-list'), # product-list
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'), # get product
    path('products/search/', ProductSearchView.as_view(), name='product-search'), # search

    path('users/profile/', UserProfileView.as_view(), name='user-profile'), # account detail (auth)
    
    path('admin/products/', ProductAdminCreateView.as_view(), name='product-admin-create'), # create pr (admin)
    path('admin/products/<int:pk>/', ProductAdminDetailView.as_view(), name='product-admin-detail'), # edit pr (admin)
    path('admin/users/delete/<int:pk>/', UserAdminDeleteView.as_view(), name='user-admin-delete'), # user delete (admin)
    path('admin/categories/create/', CategoryCreate.as_view(), name = 'category-create' ), # create cat (admin)
    path('admin/categories/edit/<int:pk>/', CategoryEdit.as_view(), name = 'category-edit'), # edit cat (admin)
    path('admin/users/', UserListView.as_view(), name='user-list'), # users-list (admin)

    path('carts/', CartView.as_view()), # create and list the cart
    path('cart-to-order/', CartToOrderView.as_view(), name='cart-to-order-view'), # placing an order + clearing the cart
]

