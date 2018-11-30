from django.urls import path,re_path
from carts import views as carts_views

urlpatterns = [
    path('cart/', carts_views.cart_home, name='cart'),
    path('update/', carts_views.cart_update, name='update'),
    path('checkout/', carts_views.checkout_home, name='checkout'),
    path('checkout/success/', carts_views.checkout_done_view, name='success'),
]

