from django.urls import path
from .data_set_subview.view import DataSetView , GetAnalysisData,AddAnalysisData,GetAnalysisDataUser, DeleteAnalyticData
from .user_subview.view import GetUserData, UpdateUserData
app_name = 'mainApp'

urlpatterns = [
    path('data-set-get/', DataSetView.as_view(), name="data-set-get"),
    path('data-analysis-get/', GetAnalysisData.as_view(), name="data-set-get"),
    path('data-analysis-get-user/', GetAnalysisDataUser.as_view(), name="data-set-get"),
    path('data-analysis-add/', AddAnalysisData.as_view(), name="data-set-add"),
    path('data-analysis-delete/', DeleteAnalyticData.as_view(), name="data-set-delete"),

    
    path('get-user-data/', GetUserData.as_view(), name="create_user"),
    path('update-user-data/', UpdateUserData.as_view(), name="update_user"),
    
]
