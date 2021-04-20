from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomAccountManager
from django.forms.models import model_to_dict


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
# create user
class CreateUser(APIView):
    permission_classes = ()
   
    def post(self, request):
        try:
            dataReq = request.data  
            temp = CustomAccountManager().create_user(dataReq["user_name"], dataReq["password"],is_dev = dataReq["is_dev"] == "true")
            if temp is None:
                response = "User existed"
            else:
                response = "User Created 🙂" 
            return Response(response)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# create super user
class CreateSuperUser(APIView):
    permission_classes = ()
   
    def post(self, request):
        # GET data example
        dataReq = request.data
        try:
            CustomAccountManager().create_superuser(dataReq["user_name"], dataReq["password"],is_dev = dataReq["is_dev"] == "true")
            return Response("UserCreated")
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
    