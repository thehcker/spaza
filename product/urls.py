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
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from profiles import views as profiles_views
from carts import views as carts_views
from contact import views as contact_views
from addresses import views as addresses_views
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
    path('analytics/', include(('analytics.urls','analytics'),namespace='history-products')),
    path('profile/',profiles_views.userProfile,name='profile'),
    path('checkout/address/create/',addresses_views.checkout_address_create_view,name='checkout_address_create'),
    path('checkout/address/reuse/',addresses_views.checkout_address_reuse_view,name='checkout_address_reuse'),
    path('register/guest/',profiles_views.guest_register_view,name='guest_register'),
    path('profile/', profiles_views.userProfile, name='profile'),
    path('myupload/', profiles_views.model_profile_upload, name='myupload'),
    path('accounts/', include('allauth.urls')),
    path('search/', include(('search.urls','search'),namespace='search')),
    path('account/',profiles_views.AccountHomeView.as_view(),name='account'),
    
    path('reset/',auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    path('reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
    path('reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),

    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
