from django.urls import path
from .views import CategoryView, FileDownloadDemo,FileUploadDemo

app_name = 'mainApp'

urlpatterns = [
    # Process list
    path('category-list-get/', CategoryView.as_view(), name="category-list-get"),
    path('download-file/', FileDownloadDemo.as_view(), name="download-pdf"),
    path('upload-file/', FileUploadDemo.as_view(), name="upload-file"),
    
]
