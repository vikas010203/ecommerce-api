from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser, Category, Product, Order
from .serializers import UserSerializer, CategorySerializer, ProductSerializer, OrderSerializer, OrderStatusSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter, BooleanFilter
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



# ------------------------
# User Registration & Profile
# ------------------------

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# ------------------------
# Category View
# ------------------------

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ------------------------
# Product Filtering
# ------------------------

class ProductFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    in_stock = BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value:
            return queryset.filter(stock__gt=0)
        return queryset


# ------------------------
# Product View with Filters
# ------------------------

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


# ------------------------
# Order Creation
# ------------------------
class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


#------------------
# User Order List
#------------------
class UserOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).prefetch_related('items__product')


# -------------
# Update Order Status
# -------------
class UpdateOrderStatusView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        order = serializer.save()
        channel_layer = get_channel_layer()
        group_name = f"user_{order.user.id}"

        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'order_status_update',
                'order_id': order.id,
                'status': order.status
            }
        )
