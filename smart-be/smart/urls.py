"""smart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from shop import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/product/$', views.product_list),
    re_path(r'^api/product/([0-9])$', views.product_detail),
    re_path(r'^api/tshirt/$', views.tshirt_list),
    re_path(r'^api/tshirt/([0-9])$', views.tshirt_detail),
    re_path(r'^api/shoes/$', views.shoes_list),
    re_path(r'^api/shoes/([0-9])$', views.shoes_detail),
    re_path(r'^api/sweatshirt/$', views.sweatshirt_list),
    re_path(r'^api/sweatshirt/([0-9])$', views.sweatshirt_detail),
    re_path(r'^api/jeans/$', views.jeans_list),
    re_path(r'^api/jeans/([0-9])$', views.jeans_detail),
    re_path(r'^api/bag/$', views.bag_list),
    re_path(r'^api/bag/([0-9])$', views.bag_detail)

]