from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
badRequestResponse = "Bad request"
serverErrorResponse = "Server error please contact admin"

# get products detail
class TotalCost(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        dataReq = request.data
        try:
            if dataReq['id'] == 1:
                response = {'test' : 'response'}
            else:
                response = {'giang': 'test'}
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(response)