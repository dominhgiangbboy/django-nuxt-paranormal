from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from processApp.models import process, projects
from processApp.serializer import ProcessSerializer,ProcessDropdownSerializer,ProcessDataSerializer
from django.db.models import Avg, Count, Q, Sum

badRequestResponse = "Bad request"
serverErrorResponse = "Server error please contact admin"

# get projects list
class GetProcessList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            dataReq = request.data
            
            sql_requirement = ""
            if 'product_id' in dataReq:
                if dataReq['product_id'] != 0 and dataReq['product_id'] != None:
                    product_id = dataReq["product_id"]
                    sql_requirement = f"where a.product_id = {product_id}"
                    if 'plant_id' in dataReq:
                        if dataReq['plant_id'] != 0 and dataReq['plant_id'] != None:
                            plant_id = dataReq['plant_id']
                            sql_requirement =sql_requirement + f" and a.plant_id = {plant_id}"
                else:
                    if 'plant_id' in dataReq:
                        if dataReq['plant_id'] != 0 and dataReq['plant_id'] != None:
                            plant_id = dataReq['plant_id']
                            sql_requirement = f"where a.plant_id = {plant_id}"
            else:
                if 'plant_id' in dataReq:
                    if dataReq['plant_id'] != 0 and dataReq['plant_id'] != None:
                        plant_id = dataReq['plant_id']
                        sql_requirement = f"where a.plant_id = {plant_id}"
            
            listPlant = process.objects.raw(
                    f"""SELECT a.id,
                        a.plant_id
                        ,a.product_id
                        ,a.process_type
                        ,c.name AS product_name
                        ,b.name AS plant_name
                        ,d.name AS name
                        FROM fukakachi_django.processApp_process a
                        LEFT JOIN fukakachi_django.indexApp_production_plant_list b ON a.plant_id = b.id
                        LEFT JOIN fukakachi_django.processApp_products_list c ON a.product_id = c.id
                        LEFT JOIN fukakachi_django.indexApp_process_list d ON a.process_type = d.id
                        {sql_requirement}
                        """)
            serializer  = ProcessSerializer(listPlant, many= True)
            return Response(serializer.data) 
        except:
            response = badRequestResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# get projects list
class AddProcessListPlant(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            dataReq = request.data
            plant_id = dataReq["plant_id"]
            project_id = dataReq["project_id"]
            product_id = dataReq["product_id"]
            process_type = 0
            if "process_type" in dataReq:
                if dataReq["process_type"] != 0 and dataReq["process_type"] != None:
                    process_type = dataReq["process_type"]
            sql_requirement_3 = ""
            if process_type != 0:
                sql_requirement_3 = f""" or a.id = {process_type}"""
            sql_requirement = f"""WHERE project_id = {project_id}
                                    AND plant_id = {plant_id}"""
            sql_requirement_2 = f""" or product_id != {product_id} """
            listPlant = process.objects.raw(
                    f"""SELECT a.name
                               ,a.id
                            FROM (
                                SELECT *
                                FROM fukakachi_django.indexApp_process_list
                                WHERE plant_id = {plant_id}
                            ) as a
                            LEFT JOIN (
                                SELECT *
                                FROM fukakachi_django.processApp_process
                                {sql_requirement}
                                ) AS b ON a.id = b.process_type
                        where b.product_id is null {sql_requirement_2} {sql_requirement_3}
                        """)
            serializer  = ProcessDropdownSerializer(listPlant, many= True)
            return Response(serializer.data) 
        except:
            response = badRequestResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       
# add projects list
class AddProcessList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
            dataReq = request.data
        # try:
            # get the last item
            if(len(process.objects.all()) == 0):
                current_id = 1
            else:
                last_item = process.objects.last()
                current_id = last_item.id + 1
    
            # Create a new object for model
            if dataReq != []:
                try:
                    p = process.objects.create(
                            product_id=dataReq['product_id'],
                            plant_id = dataReq['plant_id'],
                            process_type = dataReq['process_type'],
                            project_id=dataReq['project_id'], 
                            id = current_id,
                    )
                except:
                    response = badRequestResponse
           
            listProject = process.objects.raw(
                    f"""SELECT a.id,
                        a.plant_id
                        ,a.product_id
                        ,a.process_type
                        ,c.name AS product_name
                        ,b.name AS plant_name
                        ,d.name AS name
                        FROM fukakachi_django.processApp_process a
                        LEFT JOIN fukakachi_django.indexApp_production_plant_list b ON a.plant_id = b.id
                        LEFT JOIN fukakachi_django.processApp_products_list c ON a.product_id = c.id
                        LEFT JOIN fukakachi_django.indexApp_process_list d ON a.process_type = d.id
                        where a.id = {current_id}
                        """)
            serializer  = ProcessSerializer(listProject, many= True)
            response = serializer.data
            return Response(response)
        # except:
        #     response = serverErrorResponse
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# delete project
class DeleteProcessList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    p = process.objects.filter(id = dataReq["id"]).delete()
                except:
                    response = badRequestResponse
           
            response = "Delete list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# update
class UpdateProcessList(APIView):
    # Add project example
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    p = process.objects.filter(id = dataReq["id"]).update(
                        product_id=dataReq['product_id'],
                        plant_id = dataReq['plant_id'],
                        process_type = dataReq['process_type'],
                        project_id=dataReq['project_id'],
                    )
                except:
                    response = badRequestResponse
           
            response = "Update list successfully"
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# get projects list
class GetProcessDataFukakachi(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            dataReq = request.data
            
            sql_requirement = ""
            if 'project_id' in dataReq:
                if dataReq['project_id'] != 0 and dataReq['project_id'] != None:
                    project_id = dataReq["project_id"]
                    sql_requirement = f"where a.project_id = {project_id}"
            
            listPlant = process.objects.raw(
                    f"""SELECT 
                            a.id,
                            b.name,
                            c.name product_name,
                            a.一台当たりの付加価値額 ,
                            a.付加価値額 ,
                            a.実行予算金額 ,
                            a.日当りの目標付加価値額 ,
                            a.日当りの目標生産数量 ,
                            a.比率 ,
                            a.部材点数 
                        FROM  fukakachi_django . processApp_process  a 
                        left join fukakachi_django.indexApp_process_list b on a.process_type = b.id
                        left join fukakachi_django.processApp_products_list c on a.product_id = c.id
                        {sql_requirement}
                        """)
            serializer  = ProcessDataSerializer(listPlant, many= True)
            return Response(serializer.data) 
        except:
            response = badRequestResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# get projects list
class UpdateProcessDataFukakachi(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        # try:
            dataReq = request.data
            
            sql_requirement = ""
            if 'project_id' in dataReq:
                projectID = dataReq['project_id']
            if 'plant_id' in dataReq:
                plantID = dataReq['plant_id']
            if 'id' in dataReq:
                idUpdate = dataReq["id"]
            listPlant = process.objects.filter(id = idUpdate).update(
                    実行予算金額 = dataReq["実行予算金額"],
                    部材点数 = dataReq["部材点数"],
                    日当りの目標生産数量 = dataReq["日当りの目標生産数量"],
                )
            listCalculate = process.objects.filter(Q(project_id = projectID))
            for element in listCalculate:
                self.calculateData(element.id,projectID)
            
    
            return Response("successfully calculated") 
        # except:
        #     response = badRequestResponse
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # get products detail

    def calculateData(self,id, project_id):
        total_実行予算金額 =  process.objects.filter(Q(project_id = project_id)).aggregate(total=Sum('実行予算金額'))
        total = total_実行予算金額["total"]
        temp = process.objects.filter(id = id)
        
        実行予算金額 = temp[0].実行予算金額
        部材点数 = temp[0].部材点数
        日当りの目標生産数量 = temp[0].日当りの目標生産数量
        if 実行予算金額 != 0 and 実行予算金額 != None:
            # 比率 update calculate
            
            if 実行予算金額 != 0 and total != 0:
                比率 = 実行予算金額/total
            print(比率)
            listPlant = process.objects.filter(id = id).update(
                比率 = round(比率,2)*100,
            )
            
            temp = projects.objects.filter(Q(id = project_id)).aggregate(total=Sum('総付加価値額'))
            総付加価値額 = temp["total"]
            # 付加価値額 Update calculate
            if  比率 != 0:
                付加価値額 =比率*総付加価値額
                listPlant = process.objects.filter(id = id).update(
                    付加価値額 = round(付加価値額),
                )
                # 一台当たりの付加価値額 Dx/Ex
                if 部材点数 != 0 and 付加価値額 != 0:
                    一台当たりの付加価値額 = 付加価値額/部材点数
                    listPlant = process.objects.filter(id = id).update(
                        一台当たりの付加価値額 = round(一台当たりの付加価値額),
                    )
                    # 一台当たりの付加価値額 Dx/Ex
                    if 日当りの目標生産数量 != 0 and 一台当たりの付加価値額 != 0:
                        日当りの目標付加価値額 = round(一台当たりの付加価値額*日当りの目標生産数量)
                        listPlant = process.objects.filter(id = id).update(
                            日当りの目標付加価値額 = round(日当りの目標付加価値額),
                        )
                        temp = process.objects.filter(Q(project_id = project_id)).aggregate(total=Sum('日当りの目標付加価値額'))
                        projectTemp = projects.objects.filter(Q(id = project_id))
                        projects.objects.filter(Q(id = project_id)).update(一日当り付加価値額収支 = temp["total"] - projectTemp[0].一日当り必要固定費額)


class getCalculateTotalData(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        dataReq = request.data
        try:
            if "project_id" in dataReq:
                project_id = dataReq['project_id']
            if dataReq['project_id'] == 1:
                response = {'test' : 'response'}
            else:
                response = {'giang': 'test'}
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(response)