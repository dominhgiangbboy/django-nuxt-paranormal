
import os
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
        # try:
            dataReq = request.data
            response = ''
            if(dataReq["category_id"]!=0 and dataReq["type_id"]!=0):      
                temp = data_set.objects.filter(
                    type_id = dataReq["type_id"]
                    , category_id = dataReq["category_id"]
                )
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
            if(dataReq["category_id"]==0 and dataReq["type_id"]!=0):      
                temp = data_set.objects.filter(type_id = dataReq["type_id"])
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
            if(dataReq["category_id"]!=0 and dataReq["type_id"]==0):      
                temp = data_set.objects.filter(category_id = dataReq["category_id"])
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
            if(dataReq["category_id"]==0 and dataReq["type_id"]==0):      
                temp = data_set.objects.all()
                response = temp
                temp2 = 0
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    response = temp2.data
                return Response(response)
        # except:
        #     response = "Server error please contact admin"
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Get data set detailed data
class GetAnalysisData(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        def retrieve_file_paths(dirName):
    
        # setup file paths variable
            filePaths = []
            
            # Read all directory, subdirectories and file lists
            for root, directories, files in os.walk(dirName):
                for filename in files:
                    filePath = os.path.join(root, filename)
                    filePaths.append(
                        {
                            'name': filename,
                            'file': 'video',
                            'path': filePath,
                        },
                    )
                    
            # return all paths
            return filePaths
        try:
            dataReq = request.data
            response = {"detail": '', "analyzed": "", "data_tree": ""}
            if(dataReq["data_set_id"]!=0):   
                # Getting dataset information
                idData = dataReq["data_set_id"]   
                temp = data_set.objects.filter(id = idData)
                if len(temp) > 0:
                    temp2 = DataSetSerializer(temp, many = True)
                    responseDetail = temp2.data
                temp3 = analyzed_data.objects.filter(data_set_id = idData)
                temp_link = retrieve_file_paths(temp[0].linkFolder)
                responseAnalyzed = []
               
                if len(temp3) > 0:
                    dataAnalyzed = AnalyzedSerializer(temp3, many = True)
                    responseAnalyzed = dataAnalyzed.data
                    
                    i = 0
                    while i < len(responseAnalyzed) :
                        user_id = responseAnalyzed[i]['user']
                        user_temp = NewUser.objects.filter(id = user_id)
                        responseAnalyzed[i]['author'] = user_temp[0].user_name
                        data_set_id = responseAnalyzed[i]['data_set']
                        responseAnalyzed[i]['data_set_id'] = data_set_id
                        i += 1

                response['detail'] = responseDetail
                response['analyzed'] = responseAnalyzed
                response['data_tree'] = temp_link
                return Response(response)
            else:      
                response = "This is not a valid data set"
                return Response(response)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Get data analyzed data
class GetAnalysisDataUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            dataReq = request.data
            responseAnalyzed = []
            if dataReq['user_id'] != 0:
                response = ''
                temp3 = analyzed_data.objects.filter(user_id = dataReq['user_id'])
                if len(temp3) > 0:
                    dataAnalyzed = AnalyzedSerializer(temp3, many = True)
                    responseAnalyzed = dataAnalyzed.data
                    
                return Response(responseAnalyzed)
            else:      
                response = "This is not a valid data set"
                return Response(response)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddAnalysisData(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            dataReq = request.data
            if(dataReq["user_id"]!=0):   
                # Getting dataset information
                temp3 = analyzed_data.objects.create(
                    **dataReq
                )
                response = ''
                return Response(response)
            else:      
                response = "This is not a valid data"
                return Response(response)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DeleteAnalyticData(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            dataReq = request.data
            id = dataReq["id"]
            if(id!=0):   
                # Getting dataset information
                temp3 = analyzed_data.objects.filter(id = id).delete()
                response = ''
                return Response(response)
            else:      
                response = "This is not a valid data"
                return Response(response)
        except:
            response = "Delete error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)