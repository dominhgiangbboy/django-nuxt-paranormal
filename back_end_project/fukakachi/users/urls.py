from django.urls import path
from .views import CreateUser,MyTokenObtainPairView

app_name = 'users'

urlpatterns = [
    path('create-user/', CreateUser.as_view(), name="create_user"),
    path('login/', MyTokenObtainPairView.as_view(), name="login"),
]
