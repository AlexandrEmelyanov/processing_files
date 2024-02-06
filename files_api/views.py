import logging

from django.http import HttpResponseServerError
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser

from .models import File
from .paginations import FileListPagination
from .serializers import FileSerializer

logger = logging.getLogger(__name__)


class FilesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns -> list of all files.
    Specific file access is also available: /files/<id>/
    Permission -> read-only.
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = FileListPagination


class FileUpLoadAPIView(CreateAPIView):
    """
    Implemented the Post method for adding files to the server.
    After the method is executed, the File object processing is started in 'signals.py'.

    Return -> serialized data (if the data is valid, it is saved on the server)
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        try:
            response = self.create(request, *args, **kwargs)
            file_id = response.data['id']
            logger.info(f'The file #{file_id} was successfully saved to the server')
            return response
        except Exception as e:
            logger.error(f'An error occurred while saving the file: {str(e)}')
            return HttpResponseServerError()
