import logging

from rest_framework import viewsets

from .models import File
from .paginations import FileListPagination
from .serializers import FileSerializer
from .permissions import IsAdminOrReadOnly

logger = logging.getLogger(__name__)


class FilesViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = FileListPagination
    permission_classes = (IsAdminOrReadOnly,)

