"""pazar_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.urls import path

from restaurant import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('register', views.user_register, name='register'),
    path('registeration', views.registeration_view, name='registeration'),
    path('add-product-wish-list', views.add_product_wish_list, name='add_product_wish_list'),
    path('place-order', views.place_order_view, name='place_order_view'),
    path('promo/apply', views.apply_coupon, name='place_order_view'),
    path('search', views.search, name='search'),
    path('user-info/', views.user_info, name='register'),
]
