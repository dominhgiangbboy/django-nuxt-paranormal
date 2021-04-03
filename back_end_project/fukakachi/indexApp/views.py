from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from indexApp.models import production_plant_list, sub_process_list, process_list
from .serializer import  ProcessListSerializer,ProductPlantSerializer,SubProcessListSerializer
from django.db.models import Avg, Count, Q, Sum
import json
# Process List operations
class GetProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        try:
            dataReq = request.data
            _plantID = 0
            if "plant_id" in dataReq:
                _plantID = dataReq["plant_id"]
                listData = process_list.objects.raw(f""" SELECT *,b.name as 工場  FROM fukakachi_django.indexApp_process_list a
                                                        left join fukakachi_django.indexApp_production_plant_list b on  a.plant_id = b.id where a.plant_id = {_plantID}""")
            else:
                listData = process_list.objects.raw(""" SELECT *,b.name as 工場  FROM fukakachi_django.indexApp_process_list a
                                                        left join fukakachi_django.indexApp_production_plant_list b on  a.plant_id = b.id""")
            serializer  = ProcessListSerializer(listData, many= True)
            return Response(serializer.data)
        except Exception:
            response = "Bad request"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class AddProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # Add data example
        try:
            dataReq = request.data
            last_item = process_list.objects.last()
            # get the last item
            if(len(process_list.objects.all()) == 0):
                current_id = 1
            else:
                current_id = last_item.id + 1

            process_list.objects.create(name=dataReq['name'], id = current_id, plant_id = dataReq["plant_id"], 大工程番号 = dataReq["大工程番号"])
           
            return Response("Created")
        except Exception:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DeleteProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # delete data example
        try:
            dataReq = request.data
            process_list.objects.filter(id = dataReq['id']).delete()
            return Response('Delete process success')
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # update data example
        try:
            dataReq = request.data
            process_list.objects.filter(id = dataReq['id']).update(name=dataReq['name'], plant_id = dataReq["plant_id"], 大工程番号 = dataReq["大工程番号"])
            return Response('Update process success')
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Process List operations
class GetSubProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        try:
            dataReq = request.data
            if "id_process" in dataReq:
                listData = sub_process_list.objects.filter(id_process = dataReq["id_process"])
            elif "process_id" in dataReq:
                listData = sub_process_list.objects.filter(~Q(id_process = dataReq["process_id"]))
            else:
                listData = sub_process_list.objects.all()
            serializer  = SubProcessListSerializer(listData, many= True)
            return Response(serializer.data)
        except Exception:
            response = "Bad request"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class AddSubProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # Add data example
        try:
            dataReq = request.data
            last_item = sub_process_list.objects.last()
            # get the last item
            if(len(sub_process_list.objects.all()) == 0):
                current_id = 1
            else:
                current_id = last_item.id + 1
            if "process_id" in dataReq:
                sub_process_list.objects.filter(id = dataReq["id"]).update( id_process =dataReq['process_id'])
            else:
                sub_process_list.objects.create(name=dataReq['name'],程番号 =dataReq["程番号"] ,id = current_id)
            
            listPk = sub_process_list.objects.filter(id = current_id)
            serializer  = SubProcessListSerializer(listPk, many= True)
            return Response(serializer.data)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class DeleteSubProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # delete data example
        try:
            dataReq = request.data
            if "id_process" in dataReq:
                sub_process_list.objects.filter(Q(id = dataReq['id'])).update(
                    id_process = 0
                )
            else:
                sub_process_list.objects.filter(Q(id = dataReq['id'])).delete()
            return Response('Delete process success')
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateSubProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # update data example
        try:
            dataReq = request.data
            if "process_id" in dataReq:
                sub_process_list.objects.filter(Q(id = dataReq['id'])).update(
                    id_process = dataReq["process_id"]
                )
                sub_process_list.objects.filter(Q(id = dataReq['current_id'])).update(
                    id_process = 0
                )
            else:
                sub_process_list.objects.filter(Q(id = dataReq['id'])).update(
                    name = dataReq['name'],
                    程番号 = dataReq['程番号'],
                )
            return Response('Update process success')
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Get plant list
class GetPlantList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
      #   get cost list
    def post(self, request):
        # GET data example
        try:
            dataReq = request.data
            listPk = production_plant_list.objects.all()
            serializer  = ProductPlantSerializer(listPk, many= True)
        except:
            response = "Bad request"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)

class AddPlantList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    # add cost list
    def post(self, request):
        # Update data example
        try:
            dataReq = request.data
            last_item = production_plant_list.objects.last()
            # get the last item
            if(len(sub_process_list.objects.all()) == 0):
                current_id = 1
            else:
                current_id = last_item.id + 1
            p = production_plant_list.objects.create(name=dataReq['name'], id = current_id)
            listPk = production_plant_list.objects.filter(id = current_id)
            serializer  = ProductPlantSerializer(listPk, many= True)
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)

class DeletePlantList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # delete data example
        try:
            dataReq = request.data
            production_plant_list.objects.filter(id = dataReq['id']).delete()
            return Response('Delete process success')
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdatePlantList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
       # update data example
        try:
            dataReq = request.data
            production_plant_list.objects.filter(id = dataReq['id']).update(name=dataReq['name'])
            return Response('Update process success')
        except:
            response = "Server error please contact admin"
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)