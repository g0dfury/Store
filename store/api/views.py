from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *

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
    
# Поиск +
class ProductSearchView(generics.ListAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Product.objects.filter(name__icontains=query)

# Корзина

class CartCreate(generics.ListCreateAPIView): # создать отобразить корзмну
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class CartList(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cart_id = self.kwargs.get('cart_id', None)
        
        if cart_id:
            user_cart = Cart.objects.get(pk=cart_id)
        else:
            user_cart, created = Cart.objects.get_or_create(user=user)

        serializer.save(cart=user_cart)

    def create(self, request, *args, **kwargs):
        data = request.data
        cart_id = kwargs.get('cart_id', None)
        
        if cart_id:
            user_cart = Cart.objects.get(pk=cart_id)
        else:
            user_cart, created = Cart.objects.get_or_create(user=request.user)

        serializer = CartItemSerializer(data=data, many=True, context={'cart': user_cart})
        
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save(cart=user_cart)  # Убедимся, что передаем cart в save()

            added_items = serializer.validated_data  # Получаем данные добавленных товаров
            items_info = [
                f"{item['product'].name} ({item['quantity']} units)" for item in added_items
            ]
            items_message = f"Item(s) added to cart successfully: {', '.join(items_info)}"

            return Response({'success': True, 'message': items_message}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'success': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    # permission_classes = [permissions.IsAuthenticated]