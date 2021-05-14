from django.urls import path
from .data_set_subview.view import DataSetView , GetAnalysisData,AddAnalysisData,GetAnalysisDataUser
from .user_subview.view import GetUserData
app_name = 'mainApp'

urlpatterns = [
    path('data-set-get/', DataSetView.as_view(), name="data-set-get"),
    path('data-analysis-get/', GetAnalysisData.as_view(), name="data-set-get"),
    path('data-analysis-get-user/', GetAnalysisDataUser.as_view(), name="data-set-get"),
    path('data-analysis-add/', AddAnalysisData.as_view(), name="data-set-add"),

    
    path('get-user-data/', GetUserData.as_view(), name="create_user"),
    
]
