from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Category, Product, Review, Cart, CartItem, Order, OrderItem
from .serializers import (
    CategorySerializer, ProductSerializer, ReviewSerializer,
    CartSerializer, OrderSerializer,
)


# Категории: +

class CategoryList(generics.ListCreateAPIView): # отображение + создание категории
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):    # достать, обновить или удалить категорию
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Товары +

class ProductList(generics.ListCreateAPIView):  # отобразить и создать продукт
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView): # достать обновить удалить продукт
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductByCategoryList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
    

# Обзоры

class ReviewList(generics.ListCreateAPIView):  # отобразить создать обзор
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView): # достать обновить удалить обзор
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

# Корзина

class CartList(generics.ListCreateAPIView): # создать отобразить корзмну
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

class CartDetail(generics.RetrieveUpdateDestroyAPIView):  # достать обновить удалить корзину
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

# Заказы

class OrderList(generics.ListCreateAPIView): # создать отобразить заказ
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):  # достать обновить удалить заказ
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

# Поиск +
class ProductSearchView(generics.ListAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Product.objects.filter(name__icontains=query)

# Истрия заказов
class OrderHistoryView(generics.ListAPIView): 
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)
