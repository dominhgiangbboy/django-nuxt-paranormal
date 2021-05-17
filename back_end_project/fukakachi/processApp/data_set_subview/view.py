
from django.db.models import manager
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from processApp.models import data_set , analyzed_data
from users.models import  NewUser
from processApp.serializer import DataSetSerializer , AnalyzedSerializer
# Get data set list
class DataSetView(APIView):
    permission_classes = [IsAuthenticated]
   
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

# Get data set detailed data
class GetAnalysisData(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # try:
            dataReq = request.data
            response = {"detail": '', "analyzed": ""}
            if(dataReq["dataSetID"]!=0):   
                # Getting dataset information
                idData = dataReq["dataSetID"]   
                temp = data_set.objects.filter(id = idData)
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    responseDetail = temp2.data
                temp3 = analyzed_data.objects.filter(dataSetID = idData)
                if len(temp3) > 0:
                    dataAnalyzed = AnalyzedSerializer(temp3, many = True)
                    responseAnalyzed = dataAnalyzed.data
                    i = 0
                    while i < len(responseAnalyzed) :
                        temp = NewUser.objects.filter(id = responseAnalyzed[i]["userID"])
                        userName = ''
                        if len(temp) > 0:
                            userName = temp[0].user_name
                        responseAnalyzed[i]['author'] = userName
                        i += 1

                response['detail'] = responseDetail
                response['analyzed'] = responseAnalyzed
                return Response(response)
            else:      
                response = "This is not a valid data set"
                return Response(response)
        # except:
        #     response = "Server error please contact admin"
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Get data analyzed data
class GetAnalysisDataUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # try:
            dataReq = request.data
            if dataReq['userID'] != 0:
                response = ''
                temp3 = analyzed_data.objects.filter(userID = dataReq['userID'])
                if len(temp3) > 0:
                    dataAnalyzed = AnalyzedSerializer(temp3, many = True)
                    responseAnalyzed = dataAnalyzed.data
                    
                return Response(responseAnalyzed)
            else:      
                response = "This is not a valid data set"
                return Response(response)
        # except:
        #     response = "Server error please contact admin"
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddAnalysisData(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # try:
            dataReq = request.data
            if(dataReq["userID"]!=0):   
                # Getting dataset information
                temp3 = analyzed_data.objects.create(
                    **dataReq
                )
                response = ''
                return Response(response)
            else:      
                response = "This is not a valid data set"
                return Response(response)
        # except:
        #     response = "Server error please contact admin"
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)