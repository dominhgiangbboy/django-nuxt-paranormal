
from django.db.models import manager
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from processApp.models import  data_set , analyzed_data
from users.models import  NewUser
from processApp.serializer import UserSerializer 
# Get data set list
class GetUserData(APIView):
    permission_classes = [IsAuthenticated]
   
    def post(self, request):
        try:
            dataReq = request.data
            print(dataReq)
            if(dataReq["userID"]!=0):      
                temp = NewUser.objects.filter(id = dataReq["userID"])
                response = UserSerializer(temp, many = True)
                return Response(response.data)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
