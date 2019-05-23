
from django.urls import path,re_path
from products import views as products_views

urlpatterns = [
    path('', products_views.product_list_view, name='list'),
    #re_path('(?P<slug>[\w-]+)/$', products_views.product_detail_slug_view, name='detail'),
    re_path('(?P<slug>[\w-]+)/$', products_views.ProductDetailSlugView.as_view(), name='detail'),

]

