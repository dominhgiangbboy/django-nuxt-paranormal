
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import FileResponse, response
from .models import data_category
from .serializer import CategorySerializer
from django.core.files.storage import FileSystemStorage
from shutil import make_archive
import os
import zipfile
# create user
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
            return Response('No data')
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
                    # Create the full filepath by using os module.
                    filePath = os.path.join(root, filename)
                    filePaths.append(filePath)
                    
            # return all paths
            return filePaths
        dataReq = request.data
        dir_name = dataReq["linkFolder"]
        print(dir_name)
        # Call the function to retrieve all files and folders of the assigned directory
        try: 
            if os.path.isfile(dir_name+'.zip'):
                zip = open(dir_name+'.zip','rb')    
                return FileResponse(zip, filename="ab.zip")
            else:
                filePaths = retrieve_file_paths(dir_name)
                    # printing the list of all files to be zipped
                print('The following list of files will be zipped:')
                for fileName in filePaths:
                    print(fileName)
                    
                # writing files to a zipfile
                zip_file = zipfile.ZipFile(dir_name+'.zip', 'w')
                with zip_file:
                    # writing each file one by one
                    for file in filePaths:
                        zip_file.write(file)
                zip = open(dir_name+'.zip','rb')    
                return FileResponse(zip,  filename="ab.zip")
        
        except:
            response = "Error downloading file"
            return Response(response , status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FileUploadDemo(APIView):
    permission_classes = []
    def post(self, request):
        try:
            myfile = request.FILES['file']
            fs = FileSystemStorage(location='/Users/giang/Documents/GitHub/django-nuxt-paranormal/back_end_project/fukakachi/assets') #defaults to   MEDIA_ROOT  
            filename = fs.save(myfile.name, myfile)
            return Response('Success')
        except:
            response = "Error downloading file"
            return Response(response , status=status.HTTP_500_INTERNAL_SERVER_ERROR)