
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import data, data_set
from .serializer import DataSetSerializer
# create user
class DataSetView(APIView):
    permission_classes = []
   
    def post(self, request):
        # try:
            dataReq = request.data  
            temp = data_set.objects.all()
            response = temp
            if len(temp) > 0:
                response = DataSetSerializer(temp).data
            
            return Response(response)
        # except:
        #     response = "Server error please contact admin"
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)