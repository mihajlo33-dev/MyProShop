from django.contrib import admin
from django.urls import path, re_path
from shop import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

]