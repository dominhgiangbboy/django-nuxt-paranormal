
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from processApp.models import products_list, projects,detailed_cost
from processApp.serializer import ProductSerializer
# from indexApp.models import product_process_list
#from indexApp.serializer import CostListSerializer
from django.db.models import Avg, Count, Q, Sum
# get products list
badRequestResponse = "Bad request"
serverErrorResponse = "Server error please contact admin"
class GetProductList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        dataReq = request.data
        sql_string = """SELECT b.name AS project_name
                            ,a.name
                            ,a.id
                            ,a.project_id
                        FROM fukakachi_django.processApp_products_list AS a
                        LEFT JOIN fukakachi_django.processApp_projects AS b ON b.id = a.project_id"""
        if 'project_id' in dataReq:
            if dataReq['project_id'] != 0 and dataReq['project_id'] != None:
                project_id = dataReq['project_id']
                sql_string = sql_string + f' where a.project_id = {project_id}'
                if 'product_id' in dataReq:
                    if dataReq['product_id'] != 0 and dataReq['product_id'] != None:
                        product_id = dataReq['product_id']
                        sql_string = sql_string + f' and a.id = {product_id}'
        else:
            if 'product_id' in dataReq:
                if dataReq['product_id'] != 0 and dataReq['product_id'] != None:
                    product_id = dataReq['product_id']
                    sql_string = sql_string + f' where a.id = {product_id}'
        try:
            dataRes = products_list.objects.raw(sql_string)
            serializer  = ProductSerializer(dataRes, many= True)
            response = serializer.data
            return Response(response)
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# get products list
class AddProductsList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # get the last item
            if(len(products_list.objects.all()) == 0):
                current_id = 1
            else:
                last_item = products_list.objects.last()
                current_id = last_item.id + 1
            sql_string = f"""SELECT b.name AS project_name
                            ,a.name
                            ,a.id
                            ,a.project_id
                        FROM fukakachi_django.processApp_products_list AS a
                        LEFT JOIN fukakachi_django.processApp_projects AS b ON b.id = a.project_id where a.id = {current_id}"""
            # Create a new object for model
            if dataReq != []:
                try:
                    p = products_list.objects.create(
                        name=dataReq['name'],
                        project_id = dataReq['project_id'], 
                        id = current_id
                    )
                except:
                    response = badRequestResponse
                    return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                dataRes = products_list.objects.raw(sql_string)
                serializer  = ProductSerializer(dataRes, many= True) 
                response = serializer.data
                return Response(response)
                
            else:
                response = badRequestResponse
                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             # add default cost Items list
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

# get products list
class DeleteProductsList(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
           
            # Create a new object for model
            if dataReq != []:
                
                dataRes = products_list.objects.filter(id = dataReq["id"]).delete()
                return Response(dataRes)
                
            else:
                response = badRequestResponse
                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             # add default cost Items list
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  