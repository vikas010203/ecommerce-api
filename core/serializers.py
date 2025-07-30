from rest_framework import serializers
from .models import CustomUser, Category, Product, Order, OrderItem



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'address', 'phone', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']
        read_only_fields = ['price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'status', 'created_at', 'updated_at', 'items']
        read_only_fields = ['user', 'total_price', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        order = Order.objects.create(user=user)

        total = 0
        for item in items_data:
            product = item['product']
            quantity = item['quantity']
            price = product.price

            if product.stock < quantity:
                raise serializers.ValidationError(f"Not enough stock for {product.name}")

            # Reduce stock
            product.stock -= quantity
            product.save()

            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total += price * quantity

        order.total_price = total
        order.save()
        return order



class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
