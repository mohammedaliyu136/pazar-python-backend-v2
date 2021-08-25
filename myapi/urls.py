from django.urls import path, include
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from myapi.core import views
from .api import router

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/restaurant/', include('restaurant.urls')),
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
