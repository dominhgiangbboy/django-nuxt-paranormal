from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.db.models import  Q, Sum

from processApp.models import products_list, projects,detailed_cost
from processApp.serializer import DetailedCostSerializer

badRequestResponse = "Bad request"
serverErrorResponse = "Server error please contact admin"




class ListDetailedCost(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    #   get cost list
    def post(self, request):
        # GET data example
        try:
            idReq = request.data['product_id']
            dataRes = detailed_cost.objects.raw(f'SELECT * FROM abnormal_django.processApp_detailed_cost where product_id = {idReq}; ')
            serializer  = DetailedCostSerializer(dataRes, many= True) 
        except:
            response = serverErrorResponse
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.data)
class UpdateListDetailedCost(APIView):
    permission_classes = (IsAuthenticated,  IsAdminUser)
    def post(self,request):
            dataReq = request.data
        # try:
            
            # get the last item
            last_item = detailed_cost.objects.last()
            # update model by id
            product_id = dataReq[0]['product_id']
            productsList = products_list.objects.get(id = product_id)
            ton_value = 0
            #  契約金額
            契約金額 =  productsList.契約金額
            # 部門間接比率
            部門間接比率 = productsList.部門間接比率


            if productsList.総ｔｏｎ数 == 0:
                response = "Please insert 総ｔｏｎ数 's value"
                return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                ton_value = productsList.総ｔｏｎ数
            for data in dataReq:
                if data != []:
                    # try:
                        temp = detailed_cost.objects.filter(id = data['id']).update(
                            営業予算金額=data['営業予算金額'],
                            実行予算金額=data['実行予算金額'],
                            実行原価金額=data['実行原価金額'],
                        )
                       
                        # calculate the data ｔｏｎ当り実行予算金額      円/ｔｏｎ .... 
                        営業予算金額_calculated = 0
                        実行予算金額_calculated = 0
                        実行原価金額_calculated = 0
                        実行予算対原価差異_calculated = 0
                        # Dx/I2
                        if data['営業予算金額'] != 0:
                            営業予算金額_calculated = data['営業予算金額']/ton_value
                        # Fx/I2
                        if data['実行予算金額'] != 0:
                            実行予算金額_calculated = data['実行予算金額']/ton_value
                        # Hx/I2
                        if data['実行原価金額'] != 0:
                            実行原価金額_calculated= data['実行原価金額']/ton_value
                        # Fx - Hx 
                        if data['実行原価金額'] != 0 and data['実行予算金額'] != 0:
                            実行予算対原価差異_calculated = data['実行予算金額'] - data['実行原価金額']
                        # update the calculated data
                        temp2 = detailed_cost.objects.filter(id = data['id']).update(
                            営業予算金額_calculated=営業予算金額_calculated,
                            実行予算金額_calculated=実行予算金額_calculated,
                            実行原価金額_calculated=実行原価金額_calculated,
                            実行予算対原価差異_calculated=実行予算対原価差異_calculated,
                        )
                        
                    # except:
                    #     response = badRequestResponse
                    #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # Get value for the H68 cols 原価総額
            total_cost_object =  detailed_cost.objects.filter(~Q(group_name = '工場溶接費内訳')&~Q(group_name = '工場加工費内訳')).aggregate(total=Sum('実行原価金額'))
            total_cost = total_cost_object['total']
            # Update 工場加工費
            self.update_group_total_field('工場加工費内訳', '工場加工費', product_id, ton_value)
            # Update 工場溶接費☆
            self.update_group_total_field('工場溶接費内訳', '工場溶接費☆', product_id, ton_value)

            # 契約金額
            部門間接費 = float(契約金額)*部門間接比率
            部門間接費_calculated = 部門間接費/ton_value
            実行予算対原価差異_部門間接費_calculated = 0
            field_object = detailed_cost.objects.filter(Q(product_id = product_id) & Q(name='部門間接費')).update(
                営業予算金額=部門間接費,
                実行予算金額=部門間接費,
                実行原価金額=部門間接費,
                営業予算金額_calculated=部門間接費_calculated,
                実行予算金額_calculated=部門間接費_calculated,
                実行原価金額_calculated=部門間接費_calculated,
                実行予算対原価差異_calculated=実行予算対原価差異_部門間接費_calculated,
            )
            # compute 法定福利費
            temp = detailed_cost.objects.get(Q(product_id = product_id) & Q(name='建方重機費'))
            D52 = temp.営業予算金額
            temp = detailed_cost.objects.get(Q(product_id = product_id) & Q(name='建方鳶工費'))
            D53 = temp.営業予算金額
            temp = detailed_cost.objects.get(Q(product_id = product_id) & Q(name='現場鍛冶工費（調整）'))
            D55 = temp.営業予算金額
            temp = detailed_cost.objects.get(Q(product_id = product_id) & Q(name='本締費＆ﾀｯﾁｱｯﾌﾟ費'))
            D56 = temp.営業予算金額
            temp = detailed_cost.objects.get(Q(product_id = product_id) & Q(name='現場溶接費　柱　　ｍ　梁　　ｍ'))
            D57 = temp.営業予算金額
            D62  = 0.16*(0.23*D52 + D53 + D55 + D56 +D57)
            print('D62', D62)
            field_object = detailed_cost.objects.filter(Q(product_id = product_id) & Q(name='法定福利費')).update(
                営業予算金額=D62,
        
            )
            # compute 原価総額
            self.update_total_value(product_id, ton_value)
            # add value to 構成比_calculated
            for data in dataReq:
                if data != []:
                    try:
                        構成比_calculated = 0
                        if(data['実行原価金額'] != 0 and total_cost != 0):
                           構成比_calculated = data['実行原価金額']/total_cost
                        # update the calculated data
                        tempData = detailed_cost.objects.filter(id = data['id']).update(
                            構成比_calculated=構成比_calculated,
                        )
                    except:
                        return Response(badRequestResponse, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            dataRes = detailed_cost.objects.raw(f'SELECT * FROM abnormal_django.processApp_detailed_cost where product_id = {product_id}; ')
            serializer  = DetailedCostSerializer(dataRes, many= True) 
            response = serializer.data
            return Response(response)
        # except:
        #     response = serverErrorResponse
        #     return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # update total sum function
    def update_total_value(self, product_id, ton_value):
        # Update total field
        try:
            sum_object =  detailed_cost.objects.filter(~Q(group_name = '工場溶接費内訳')&~Q(group_name = '工場加工費内訳')&~Q(name = '原価総額')&~Q(name = '売上総利総額')&~Q(name = '損益分岐受注額')).aggregate(Sum('営業予算金額'), Sum('実行予算金額'),Sum('実行原価金額'))
            営業予算金額 = sum_object['営業予算金額__sum']
            実行予算金額 = sum_object['実行予算金額__sum']
            実行原価金額 = sum_object['実行原価金額__sum']
            # calculate the data ｔｏｎ当り実行予算金額      円/ｔｏｎ .... 
            営業予算金額_calculated = 0
            実行予算金額_calculated = 0
            実行原価金額_calculated = 0
            実行予算対原価差異_calculated = 0
            # Dx/I2
            if 営業予算金額 != 0:
                営業予算金額_calculated = 営業予算金額/ton_value
            # Fx/I2
            if 実行予算金額 != 0:
                実行予算金額_calculated = 実行予算金額/ton_value
            # Hx/I2
            if 実行原価金額 != 0:
                実行原価金額_calculated = 実行原価金額/ton_value
            # Fx - Hx 
            if 実行予算金額 != 0 and 実行原価金額 != 0:
                実行予算対原価差異_calculated = 実行予算金額 - 実行原価金額
            # update the calculated data
            field_object = detailed_cost.objects.filter(Q(product_id = product_id) & Q(name='原価総額')).update(
                営業予算金額=営業予算金額,
                実行予算金額=実行予算金額,
                実行原価金額=実行原価金額,
                営業予算金額_calculated=営業予算金額_calculated,
                実行予算金額_calculated=実行予算金額_calculated,
                実行原価金額_calculated=実行原価金額_calculated,
                実行予算対原価差異_calculated=実行予算対原価差異_calculated,
            )
        except:
            response = 'Failed to calculate value 原価総額'
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # update Field sum function
    def update_group_total_field(self,group_name,sum_field_name, product_id, ton_value):
        # Update total field
        try:
            sum_object =  detailed_cost.objects.filter(Q(group_name = group_name)&Q(product_id = product_id)).aggregate(Sum('営業予算金額'), Sum('実行予算金額'),Sum('実行原価金額'))
            print(sum_object['営業予算金額__sum'], sum_object['実行予算金額__sum'], sum_object['実行原価金額__sum'])
            営業予算金額 = sum_object['営業予算金額__sum']
            実行予算金額 = sum_object['実行予算金額__sum']
            実行原価金額 = sum_object['実行原価金額__sum']
            # calculate the data ｔｏｎ当り実行予算金額      円/ｔｏｎ .... 
            営業予算金額_calculated = 0
            実行予算金額_calculated = 0
            実行原価金額_calculated = 0
            実行予算対原価差異_calculated = 0
            # Dx/I2
            if 営業予算金額 != 0:
                営業予算金額_calculated = 営業予算金額/ton_value
            # Fx/I2
            if 実行予算金額 != 0:
                実行予算金額_calculated = 実行予算金額/ton_value
            # Hx/I2
            if 実行原価金額 != 0:
                実行原価金額_calculated = 実行原価金額/ton_value
            # Fx - Hx 
            if 実行予算金額 != 0 and 実行原価金額 != 0:
                実行予算対原価差異_calculated = 実行予算金額 - 実行原価金額
            # update the calculated data
            field_object = detailed_cost.objects.filter(Q(product_id = product_id) & Q(name=sum_field_name)).update(
                営業予算金額=営業予算金額,
                実行予算金額=実行予算金額,
                実行原価金額=実行原価金額,
                営業予算金額_calculated=営業予算金額_calculated,
                実行予算金額_calculated=実行予算金額_calculated,
                実行原価金額_calculated=実行原価金額_calculated,
                実行予算対原価差異_calculated=実行予算対原価差異_calculated,
            )
        except:
            response = 'Failed to calculate value' + sum_field_name
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)