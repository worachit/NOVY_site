from django.urls import path, include, re_path
from . import views

app_name = "dataset"

urlpatterns = [
    path('download', views.download, name='download'),
    
    path('download/api/datasets', views.datasets, name="datasets"),

    path('download/api/drone-01/data/all', views.drone01_zip, name="zip"),
    path('download/api/drone-01/name', views.drone01_name, name="name"),
    path('download/api/drone-01/data/<str:name>', views.drone01_image, name="image"),
    path('download/api/drone-01/datac/<str:name>', views.drone01_image_compress, name="image_compress"),
    path('download/api/drone-01/label', views.drone01_label, name="label"),

    path('download/api/Marvic-15m/data/all', views.Marvic_zip, name="zip"),
    path('download/api/Marvic-15m/name', views.Marvic_name, name="name"),
    path('download/api/Marvic-15m/data/<str:name>', views.Marvic_image, name="image"),
    path('download/api/Marvic-15m/datac/<str:name>', views.Marvic_image_compress, name="image_compress"),
    path('download/api/Marvic-15m/label', views.Marvic_label, name="label"),
]
