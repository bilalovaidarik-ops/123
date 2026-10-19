from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/process/', views.process_order, name='process_order'),
    path('order-success/<int:order_id>/', views.order_success, name='order_success'),
    path('search/', views.search_products, name='search_products'),
    path('orders/', views.user_orders, name='user_orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('api/cart-count/', views.api_cart_count, name='api_cart_count'),
]
