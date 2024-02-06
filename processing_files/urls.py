from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .yasg import urlpatterns as api_docs_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('files_api.urls', namespace='files_api')),
]

# Addition API documentation
urlpatterns += api_docs_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
