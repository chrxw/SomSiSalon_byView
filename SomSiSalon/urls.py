"""SomSiSalon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from functools import cached_property
from django.contrib import admin
from django.urls import path

from index import views as index_views
from cart import views as cart_views
from delivery_detail import views as delivery_detail_views
from product import views as product_views
from service import views as service_views


urlpatterns = [
    # index all pages path
    path('admin/', admin.site.urls),
    path('', index_views.index, name='index'),
    path('cart', cart_views.index, name='cart'),
    path('delivery_detail', delivery_detail_views.index, name='delivery_detail'),
    path('product', product_views.index, name='product'),
    path('service_detail', service_views.service_index, name='service'),
    path('product_list', product_views.ProductListt.as_view(),
         name='ProductListt'),
    # path('profile'),

    path('product_detail', product_views.product_index, name='product'),

    path('best_product_seller', index_views.BestProductSeller.as_view(),
         name='BestProductSeller'),
    path('best_service_seller', index_views.BestServiceSeller.as_view(),
         name='BestServiceSeller'),

    path('mail_register_for_infomation', index_views.MailRegister.as_view(),
         name='MailRegisterForInfomation'),
]
