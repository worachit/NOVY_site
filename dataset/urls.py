from django.urls import path, include, re_path
from . import views

app_name = "dataset"

urlpatterns = [
    path('download', views.download, name='download'),
    path('download/api/drone-01/data/all', views.drone01_zip, name="zip"),
    path('download/api/drone-01/sample', views.drone01_sample, name="sample"),
    path('download/api/drone-01/name', views.drone01_sample, name="name"),
    path('download/api/drone-01/data/<str:name>', views.drone01_image, name="image"),
    path('download/api/drone-01/label', views.drone01_label, name="label"),
]
