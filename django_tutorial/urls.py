"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from store import views as store_views

urlpatterns = [
    path('', store_views.index, name='home'),
    path('product/add', store_views.product_add, name="product_add"),
    path('product/add-save', store_views.product_add_save, name="product_add_save"),
    path('product/view/<str:pk>', store_views.product_view, name="product_view"),

    path('admin/', admin.site.urls),
]
