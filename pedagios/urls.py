from django.urls import path
from .views import RegistroValePedagioAPIView, DownloadExcelAPIView

urlpatterns = [
    path('api/vale-pedagio/', RegistroValePedagioAPIView.as_view(), name='registro_vale_pedagio'),
    path('api/download-excel/', DownloadExcelAPIView.as_view(), name='download_excel'),
]
