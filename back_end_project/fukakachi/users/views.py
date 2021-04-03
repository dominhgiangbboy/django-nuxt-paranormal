from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer,MyTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from indexApp.models import roles_list
from django.core import serializers
from django.forms.models import model_to_dict
import json
from rest_framework_simplejwt.tokens import RefreshToken

# def get_tokens_for_user(user):
#     refresh = RefreshToken.for_user(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#         'userID': str(user.name),
#         'is_staff': str(user.is_staff)
#     }
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
class Login(APIView):
    permission_classes = ()
    def post(user_name,password):
        refresh = RefreshToken.for_user(user_name)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'userID': str('user_name'),
        }
class RoleList(APIView):
    permission_classes = (IsAuthenticated)
   
    def get(self, request):
        # GET data example
        dataReq = request.data
        listPk = roles_list.objects.get(name = dataReq['name'])
        data = serializers.serialize('json', [listPk,])
        struct = json.loads(data)
        return Response(struct)
    def post(self, request):
        # Update data example
        dataReq = request.data
        print(dataReq)
        listPk = roles_list.objects.get(name = dataReq['name'])
        listPk.access = dataReq['access']
        listPk.save()
        data = serializers.serialize('json', [listPk,])
        struct = json.loads(data)
        return Response(struct)