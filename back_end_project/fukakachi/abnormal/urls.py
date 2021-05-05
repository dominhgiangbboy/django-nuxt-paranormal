
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # JWT auth
    # path('', include())
    path('api/user/',include('users.urls',namespace = 'users')),
    path('api/index/',include('indexApp.urls',namespace = 'index')),
    path('api/',include('processApp.urls',namespace = 'main')),
    path('api-auth/',include('rest_framework.urls',namespace = 'rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
