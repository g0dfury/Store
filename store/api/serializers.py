from rest_framework import serializers
from .models import *

#####
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
######
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

######## 
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
    
#### 
class ProductAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

### 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']        

class UserAdminDeleteSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

### 
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemsSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()

    class Meta:
        model = CartItems
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'