from django.urls import path
from .views import GetPlantList, AddPlantList,GetProcessList, DeletePlantList,AddProcessList, DeleteProcessList,UpdatePlantList, UpdateProcessList ,GetSubProcessList,UpdateSubProcessList,DeleteSubProcessList,AddSubProcessList

app_name = 'mainApp'

urlpatterns = [
    # Process list
    path('get-process-list/', GetProcessList.as_view(), name="get_list_process"),
    path('update-process-list/', UpdateProcessList.as_view(), name="update_list_process"),
    path('delete-process-list/', DeleteProcessList.as_view(), name="delete_list_process"),
    path('add-process-list/', AddProcessList.as_view(), name="add_list_process"),

    # process product list
    path('get-sub-process-list/', GetSubProcessList.as_view(), name="get_list_sub_process"),
    path('update-sub-process-list/', UpdateSubProcessList.as_view(), name="update_list_sub_process"),
    path('delete-sub-process-list/', DeleteSubProcessList.as_view(), name="delete_list_sub_process"),
    path('add-sub-process-list/', AddSubProcessList.as_view(), name="add_list_sub_process"),
    # production plant
    path('get-plant-list/', GetPlantList.as_view(), name="list_plant"),
    path('add-plant-list/', AddPlantList.as_view(), name="add-list_plant"),
    path('update-plant-list/', UpdatePlantList.as_view(), name="update-list_plant"),
    path('delete-plant-list/', DeletePlantList.as_view(), name="delete-list_plant"),
]
