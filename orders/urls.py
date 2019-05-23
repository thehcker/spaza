
from django.urls import path,re_path
from orders import views as orders_views

urlpatterns = [
    path('', orders_views.OrderListView.as_view(), name='list'),
    #re_path('(?P<slug>[\w-]+)/$', products_views.product_detail_slug_view, name='detail'),
    re_path('(?P<order_id>[\w-]+)/$', orders_views.OrderDetailView.as_view(), name='detail'),

]

