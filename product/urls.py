"""product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as profiles_views
from carts import views as carts_views
from contact import views as contact_views
#from products import views as products_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profiles_views.index, name='index'),
    path('about/', profiles_views.about, name='about'),
    path('update/', carts_views.cart_update, name='update'),
    path('cart/', carts_views.cart_home, name='cart'),
    path('contact/',contact_views.contact,name='contact'),
    path('cart/', include(('carts.urls','carts'),namespace='carts')),
    path('list/', include(('products.urls','products'),namespace='products')),
    path('profile/',profiles_views.userProfile,name='profile'),
    path('accounts/', include('allauth.urls')),
    path('search/', include(('search.urls','search'),namespace='search')),

    #path('list/', products_views.product_list_view, name='list'),
    #path('list/<int:pk>/', products_views.product_detail_view, name='detail'),
    #re_path(r'^list/(?P<slug>[\w-]+)/$', products_views.product_detail_slug_view, name='detail'),
    #path('featured/', products_views.product_featured_list_view, name='featured'),
    #path('featured/<int:pk>/', products_views.product_featured_detail_view, name='featured-detail'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
