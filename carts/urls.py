from django.urls import path,re_path
from carts import views as carts_views

urlpatterns = [
    path('cart/', carts_views.cart_home, name='cart'),
    path('update/', carts_views.cart_update, name='update'),
]