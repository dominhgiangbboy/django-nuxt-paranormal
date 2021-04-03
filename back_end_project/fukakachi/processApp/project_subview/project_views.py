from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from processApp.models import projects,arise_cost_data
from processApp.serializer import ProjectSerializer,ProjectDataSerializer,AriseCostSerializer
from django.db.models import Avg, Count, Q, Sum
badRequestResponse = "Bad request"
serverErrorResponse = "Server error please contact admin"



# get projects list
class GetProjectsList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            listPlant = projects.objects.raw('SELECT *  FROM fukakachi_django.processApp_projects')
            serializer  = ProjectSerializer(listPlant, many= True) 
        except:
            response = badRequestResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)

# get projects list
class GetProjectsListData(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            dataReq = request.data
            if "project_id" in dataReq:
                project_id = dataReq["project_id"]
            listPlant = projects.objects.raw(f"""SELECT *  FROM fukakachi_django.processApp_projects where id = {project_id}""")
            serializer  = ProjectDataSerializer(listPlant, many= True) 
        except:
            response = badRequestResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)
# add projects list
class AddProjectsList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # get the last item
            if(len(projects.objects.all()) == 0):
                current_id = 1
            else:
                last_item = projects.objects.last()
                current_id = last_item.id + 1
    
            # Create a new object for model
            if dataReq != []:
                try:
                    
                    p = projects.objects.create(
                        name=dataReq['name'], 
                        工事名=dataReq['工事名'],
                        契約金額 = dataReq['契約金額'], 
                        材料費 = dataReq['材料費'], 
                        外注費 = dataReq['外注費'], 
                        付加価値額 = dataReq['付加価値額'], 
                        id = current_id
                    )
                except:
                    response = badRequestResponse
           
            listProject = projects.objects.raw(
                    f"SELECT * FROM fukakachi_django.processApp_projects  where id = {current_id}")
            serializer  = ProjectSerializer(listProject, many= True)
            response = serializer.data
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# delete project
class DeleteProjectsList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    p = projects.objects.filter(id = dataReq["id"]).delete()
                except:
                    response = badRequestResponse
           
            response = "Delete list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update project
class UpdateProjectsList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    p = projects.objects.filter(id = dataReq["id"]).update(
                        name=dataReq['name'], 
                        工事名=dataReq['工事名'],
                        契約金額 = dataReq['契約金額'], 
                        材料費 = dataReq['材料費'], 
                        外注費 = dataReq['外注費'], 
                        付加価値額 = dataReq['付加価値額'], 
                    )
                    self.calculateDifferent(dataReq["id"])
                except:
                    response = badRequestResponse
           
            response = "Update list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # function
    def calculateDifferent (self, project_id):       
        temp = arise_cost_data.objects.filter(project_id = project_id).aggregate(total=Sum('value'))
        total_cost = temp["total"]
        p = projects.objects.filter(id = project_id).update(
            実行予算計画後合計=total_cost     
        )
        temp2 = projects.objects.filter(Q(id = project_id)).aggregate(total=Sum('付加価値額'))
        projects.objects.filter(id = project_id).update(
            実行予算計画後合計=total_cost ,
            総付加価値額 = temp2["total"] - total_cost
        )
# add  more different
class AddAriseCostList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            # get the last item
            if(len(arise_cost_data.objects.all()) == 0):
                current_id = 1
            else:
                last_item = arise_cost_data.objects.last()
                current_id = last_item.id + 1
            if dataReq != []:
                try:
                    p = arise_cost_data.objects.create(
                        name=dataReq['name'], 
                        id=current_id,
                        value = dataReq['value'], 
                        project_id = dataReq['project_id'], 
                    )
                    temp = arise_cost_data.objects.filter(project_id = dataReq['project_id']).aggregate(total=Sum('value'))
                    total_cost = temp["total"]
                    p = projects.objects.filter(id = dataReq['project_id']).update(
                        実行予算計画後合計=total_cost     
                    )
                    temp2 = projects.objects.filter(Q(id = dataReq['project_id'])).aggregate(total=Sum('付加価値額'))
                    projects.objects.filter(id = dataReq['project_id']).update(
                        実行予算計画後合計=total_cost ,
                        総付加価値額 = temp2["total"] - total_cost
                    )
                except:
                    response = badRequestResponse
           
            response = "Add list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# add  more different
class GetAriseCostList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            # get the last item
            if(len(arise_cost_data.objects.all()) == 0):
                current_id = 1
            else:
                last_item = arise_cost_data.objects.last()
                current_id = last_item.id + 1
            if dataReq != []:
                try:
                    p = arise_cost_data.objects.filter(project_id = dataReq["project_id"])
                    serializer  = AriseCostSerializer(p, many= True) 
                    response = serializer.data
                except:
                    response = badRequestResponse
           
            
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# add  more different
class DeleteAriseCostList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    p = arise_cost_data.objects.filter(id = dataReq["id"]).delete()
                    temp = arise_cost_data.objects.filter(project_id = dataReq['project_id']).aggregate(total=Sum('value'))
                    total_cost = temp["total"]
                    p = projects.objects.filter(id = dataReq['project_id']).update(
                        実行予算計画後合計=total_cost     
                    )
                    temp2 = projects.objects.filter(Q(id = dataReq['project_id'])).aggregate(total=Sum('付加価値額'))
                    projects.objects.filter(id = dataReq['project_id']).update(
                        実行予算計画後合計=total_cost ,
                        総付加価値額 = temp2["total"] - total_cost
                    )
                    response = "Delete list successfully"
                    return Response(response)
                except:
                    response = badRequestResponse
                    return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# update project
class UpdateAriseCostList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    p = arise_cost_data.objects.filter(id = dataReq["id"]).update(
                        name=dataReq['name'], 
                        value = dataReq['value'], 
                        project_id = dataReq['project_id'],  
                    )
                    temp = arise_cost_data.objects.filter(project_id = dataReq['project_id']).aggregate(total=Sum('value'))
                    total_cost = temp["total"]
                    temp2 = projects.objects.filter(Q(id = dataReq['project_id'])).aggregate(total=Sum('付加価値額'))
                    projects.objects.filter(id = dataReq['project_id']).update(
                        実行予算計画後合計=total_cost ,
                        総付加価値額 = temp2["total"] - total_cost
                    )
                except:
                    response = badRequestResponse
           
            response = "Update list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update project
class CalculateValueMoney(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    project_id = dataReq["project_id"]
                    年間必要固定費額 = dataReq["年間必要固定費額"]

                    projects.objects.filter(id = project_id).update(
                        年間必要固定費額=年間必要固定費額 ,
                        月間必要固定費額 = round(年間必要固定費額/12),
                        一日当り必要固定費額 =  round(年間必要固定費額/12/22),
                    )
                except:
                    response = badRequestResponse
           
            response = "Update list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)