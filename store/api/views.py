from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


# category
class CategoryList(generics.ListAPIView): # отображение 
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveAPIView):    # достать категорию
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # создание (админ)

class CategoryEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  # обновить удалить получить (админ)

# products
class ProductList(generics.ListAPIView):  # отобразить и создать продукт
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView): # достать обновить удалить продукт
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductByCategoryList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Product.objects.filter(category_id=category_id)
    
# products detail (admin)
class ProductAdminCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer
    permission_classes = [permissions.IsAdminUser]

class ProductAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer
    permission_classes = [permissions.IsAdminUser]
    
# search
class ProductSearchView(generics.ListAPIView):   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Product.objects.filter(name__icontains=query)

# user details (auth)

class UserProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# profiles (admin)
class UserListView(APIView):    # list of users for admin
    permission_classes = [permissions.IsAdminUser]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)    

class UserAdminDeleteView(generics.DestroyAPIView):     # user delete for admin
    queryset = User.objects.all()
    serializer_class = UserAdminDeleteSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_destroy(self, instance):
        instance.delete()

# cart (add + list + delete)
        
class CartView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self , request):
        user = request.user
        cart = Cart.objects.filter(user = user, ordered=False).first()
        queryset = CartItems.objects.filter(cart = cart)
        serializer = CartItemsSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data
        user = request.user
        cart,_ = Cart.objects.get_or_create(user = user, ordered = False)

        product = Product.objects.get(id = data.get('product'))
        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItems(cart = cart, user = user, product = product, price = price, quantity = quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItems.objects.filter(user = user, cart = cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()

        return Response({'success': 'Items added to your cart'})    
    
    def delete(self , request):
        user = request.user
        data = request.data

        cart_item = CartItems.objects.get(id = data.get('id'))
        cart_item.delete()

        cart = Cart.objects.filter(user = user, ordered = False).first()
        queryset = CartItems.objects.filter(cart = cart)
        serializer = CartItemsSerializer(queryset, many = True)
        return Response(serializer.data)
    

# order + cart clearing    
class CartToOrderView(generics.CreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        queryset = Orders.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        cart_items = CartItems.objects.filter(user=request.user)

        if not cart_items.exists():
            return Response({'detail': 'Корзина пуста'}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = sum(item.price for item in cart_items)

        items = []
        for cart in cart_items:
            items.append(f'{cart.product}({cart.product.price} $) - {cart.quantity}')
        str_items = ', '.join(map(str, items))

        order_serializer = self.get_serializer(data={'user': request.user.id, 'cart': cart_items[0].cart.id, 'amount': total_amount, 'is_paid': True, 'items': str_items})
        order_serializer.is_valid(raise_exception=True)
        order_serializer.save()

        cart_items.delete()

        return Response(order_serializer.data, status=status.HTTP_201_CREATED)