from django.urls import path
from .views import RegisterView, ProfileView, CategoryListView, ProductListView, CreateOrderView, UserOrderListView, UpdateOrderStatusView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
    path('orders/', UserOrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/update-status/', UpdateOrderStatusView.as_view(), name='order-update-status'),




]
