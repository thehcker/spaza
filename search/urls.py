from django.urls import path,re_path
from search import views as search_views

urlpatterns = [
    path('', search_views.search_product_view, name='query'),
]
