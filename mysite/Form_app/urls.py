from django.urls import path
from . import views

urlpatterns = [
   path("file-upload/",views.file_uploader)
]