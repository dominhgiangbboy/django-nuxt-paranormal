from django.urls import path
from .views import RoleList,Login,MyTokenObtainPairView

app_name = 'users'

urlpatterns = [
    path('Role/', RoleList.as_view(), name="create_user"),
    path('login/', MyTokenObtainPairView.as_view(), name="login"),
]
