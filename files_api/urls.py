from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'files_api'

router = routers.SimpleRouter()
router.register(r'files', views.FilesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', views.FileUpLoadAPIView.as_view(), name='file_upload'),
]
