from django.urls import path
from .views import RegistroValePedagioAPIView

urlpatterns = [
    path('api/vale-pedagio/', RegistroValePedagioAPIView.as_view(), name='registro_vale_pedagio'),
]
