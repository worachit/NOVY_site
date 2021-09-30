from django.urls import path, include
from . import views

app_name = "dataset"

urlpatterns = [
    path('download', views.download, name='download'),
]