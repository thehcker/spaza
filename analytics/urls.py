from products import views as products_views
from django.urls import path

urlpatterns = [
    path('history/products/', products_views.UserProductHistoryView.as_view(), name='user-product-history'),

]