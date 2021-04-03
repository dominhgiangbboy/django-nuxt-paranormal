from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from processApp.models import products_list
from processApp.serializer import  ProductsDetailedSerializer

badRequestResponse = "Bad request"
serverErrorResponse = "Server error please contact admin"

# get products detail
class GetProductDetail(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            idReq = request.data['id']
            dataRes = products_list.objects.raw(f'select * from fukakachi_django.processApp_products_list as a where a.id = {idReq}')
            serializer  = ProductsDetailedSerializer(dataRes, many= True) 
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)

class UpdateProductDetail(APIView):
    # Add more products
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self, request):
        dataReq = request.data
        try:
            # Create a new object for model
            if dataReq != []:
                try:
                    temp = products_list.objects.filter(id = dataReq['id']).update(
                        name=dataReq['name'],
                        )
                except Exception:
                    response = badRequestResponse
                    return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            id  = dataReq['id']
            listPlant = products_list.objects.raw(
                    f'select a.id,a.name from fukakachi_django.processApp_products_list as a where a.id = {id}')
            serializer  = ProductsDetailedSerializer(listPlant, many= True)
            response = serializer.data
            return Response(response)
        except Exception:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
