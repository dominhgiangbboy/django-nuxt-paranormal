from django.urls import path
from .views import DataSetView
app_name = 'mainApp'

urlpatterns = [
    path('data-set-get/', DataSetView.as_view(), name="data-set-get"),
]
