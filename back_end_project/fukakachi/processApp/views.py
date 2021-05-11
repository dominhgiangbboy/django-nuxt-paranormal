
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import data, data_set
from .serializer import DataSetSerializer
# create user
class DataSetView(APIView):
    permission_classes = []
   
    def post(self, request):
        try:
            dataReq = request.data
            response = ''
            if(dataReq["categoryID"]!=0 and dataReq["typeID"]!=0):      
                temp = data_set.objects.filter(**dataReq)
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
            if(dataReq["categoryID"]==0 and dataReq["typeID"]!=0):      
                temp = data_set.objects.filter(typeID = dataReq["typeID"])
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
            if(dataReq["categoryID"]!=0 and dataReq["typeID"]==0):      
                temp = data_set.objects.filter(typeID = dataReq["categoryID"])
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
            if(dataReq["categoryID"]==0 and dataReq["typeID"]==0):      
                temp = data_set.objects.all()
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)