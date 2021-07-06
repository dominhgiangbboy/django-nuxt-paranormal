
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import FileResponse, response
from .models import data_category
from processApp.models import data_set
from .serializer import CategorySerializer
from django.core.files.storage import FileSystemStorage
from shutil import make_archive
import os
import zipfile
from os import path
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
# create user
class AddCategoryView(APIView):
    permission_classes = []
   
    def post(self, request):
        try:
            dataReq = request.data  
            dataReq["name"]
            temp = data_category.objects.create(name = "name", id = 1)  
            if len(temp) > 0:
                temp2 = CategorySerializer(temp, many = True)
                response = temp2.data
                return Response(response)
            return Response([])
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class CategoryView(APIView):
    permission_classes = []
   
    def post(self, request):
        try:
            dataReq = request.data  
            temp = data_category.objects.all()  
            if len(temp) > 0:
                temp2 = CategorySerializer(temp, many = True)
                response = temp2.data
                return Response(response)
            return Response([])
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class FileDownloadDemo(APIView):
    permission_classes = []
    
    def post(self, request):
        # Declare the function to return all file paths of the particular directory
        def retrieve_file_paths(dirName):
        
        # setup file paths variable
            filePaths = []
            
            # Read all directory, subdirectories and file lists
            for root, directories, files in os.walk(dirName):
                for filename in files:
                    filePath = os.path.join(root, filename)
                    filePaths.append(filePath)
                    
            # return all paths
            return filePaths
        dataReq = request.data
        dir_name = dataReq["linkFolder"]
        # Call the function to retrieve all files and folders of the assigned directory
        try: 
            if os.path.isfile(dir_name+'.zip'):
                zip = open(dir_name+'.zip','rb')  
                response = FileResponse(zip, filename="ab.zip")
                return response
            else:
                # filePaths = retrieve_file_paths(dir_name)
                
                # printing the list of all files to be zipped
                # for fileName in filePaths:
                #     print(fileName)
                # file_location2 = env("FOLDER_LINK")
                # # writing files to a zipfile
                # if not file_location2.exists('dataset'):
                #     os.mkdir('dataset')
                zip_file = make_archive('Dataset', 'zip', dir_name)
                # zip_file = zipfile.ZipFile(dir_name+'.zip', 'w', zipfile.ZIP_DEFLATED)
                # with zip_file:
                #     # writing each file one by one
                #     for file in filePaths:
                #         zip_file.write(file)
                zip = open(zip_file,'rb')    
                return FileResponse(zip,  filename="ab.zip")
        
        except:
            response = "Error downloading file"
            return Response(response , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class GetLink(APIView):
    permission_classes = []
    def post(self, request):
        dataReq = request.data
        print(dataReq)
        userID = dataReq['user_id']

        file_location2 = os.path.join(env("FOLDER_LINK"),userID)
        if not path.exists(file_location2):
            os.mkdir(file_location2)
        return Response(file_location2)

class FileUploadDemo(APIView):
    permission_classes = []
    def post(self, request):
        try:
            dataReq = request.POST
            
            dataName = dataReq['name']
            link = dataReq['link']
            type = dataReq['type']
            category = dataReq['category']
            description = dataReq['description']
            userID = dataReq['user_id']
            myfiles = request.FILES.getlist('files')
            file_location2 = os.path.join(env("FOLDER_LINK"),userID)
            if not path.exists(file_location2):
                os.mkdir(file_location2)
            file_location = os.path.join(file_location2, dataName)
            if not path.exists(file_location):
                os.mkdir(file_location)
            ## Save file
            for myfile in myfiles:
                
                fs = FileSystemStorage(location=file_location) #defaults to   MEDIA_ROOT  
                fs.save(myfile.name, myfile)
            tmp = data_set.objects.filter(linkFolder= file_location)
            tmp2 = data_set.objects.filter(name= dataName)
            if len(tmp) == 0 and len(tmp2) == 0:
                data_set.objects.create(
                    type_id = type
                    , category_id = category
                    , name = dataName
                    , description = description
                    , linkFolder = file_location
                )
            return Response('Success')
        except:
            response = "Error uploading file"
            return Response(response , status=status.HTTP_500_INTERNAL_SERVER_ERROR)