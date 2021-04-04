from django.urls import path
from .detailed_cost_subview.detailed_cost_view import ListDetailedCost, UpdateListDetailedCost
from .product_subview.product_views import GetProductList,AddProductsList,DeleteProductsList
from .project_subview.project_views import GetProjectsList,AddProjectsList, DeleteProjectsList,UpdateProjectsList,GetProjectsListData,CalculateValueMoney,AddAriseCostList,GetAriseCostList,DeleteAriseCostList,UpdateAriseCostList
from .product_detail_subview.product_detail_views import GetProductDetail, UpdateProductDetail
from .total_cost_subview.total_cost_subview import TotalCost
from .process_subview.process_views import AddProcessList,GetProcessList, AddProcessListPlant, DeleteProcessList, UpdateProcessList ,GetProcessDataabnormal ,UpdateProcessDataabnormal
app_name = 'mainApp'

urlpatterns = [
    # Project
    path('get-projects-list/', GetProjectsList.as_view(), name="get-projects-list"),
    path('add-projects-list/', AddProjectsList.as_view(), name="add_projects-list"),
    path('delete-projects-list/', DeleteProjectsList.as_view(), name="delete_projects-list"),
    path('update-projects-list/', UpdateProjectsList.as_view(), name="update_projects-list"),
    path('get-data-projects-list/', GetProjectsListData.as_view(), name="get-data_projects-list"),
    path('calculate-money/', CalculateValueMoney.as_view(), name="calculate-money"),
    # Arise cost
    path('add-arise-cost-list/', AddAriseCostList.as_view(), name="add_arise_cost-list"),
    path('get-arise-cost-list/', GetAriseCostList.as_view(), name="get_arise_cost-list"),
    path('delete-arise-cost-list/', DeleteAriseCostList.as_view(), name="del-arise-cost-list"),
    path('update-arise-cost-list/', UpdateAriseCostList.as_view(), name="update-arise-cost-list"),
    # Product list
    path('get-products-list/', GetProductList.as_view(), name="get-products-list"),
    path('add-products-list/', AddProductsList.as_view(), name="get-products-list"),
    path('delete-products-list/', DeleteProductsList.as_view(), name="delete-products-list"),
    
    # product detail
    path('get-products-detail/', GetProductDetail.as_view(), name="get-products-detail"),
    path('update-products-detail/', UpdateProductDetail.as_view(), name="update-products-detail"),
    
    # process
    path('add-process-detail/', AddProcessList.as_view(), name="add-process-detail"),
    path('get-process-detail/', GetProcessList.as_view(), name="get-process-detail"),
    path('get-process-plant/', AddProcessListPlant.as_view(), name="get-process-plant"),
    path('delete-process-detail/', DeleteProcessList.as_view(), name="delete-process-detail"),
    path('update-process-detail/', UpdateProcessList.as_view(), name="update-process-detail"),
    path('get-process-data-detail/', GetProcessDataabnormal.as_view(), name="get-process-data"),
    path('update-process-data-detail/', UpdateProcessDataabnormal.as_view(), name="update-process-data"),
    # total cost
    path('get-total-cost/', TotalCost.as_view(), name="get-total-cost"),
    # detailed cost
    path('get-table-cost/', ListDetailedCost.as_view(), name="get-table-cost"),
    path('update-table-cost/', UpdateListDetailedCost.as_view(), name="update-table-cost"),
   
]
