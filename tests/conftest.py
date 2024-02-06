import pytest

from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient


@pytest.fixture
def client(django_db_reset_sequences):
    """For test API (TestFileAPI)"""
    return APIClient()


@pytest.fixture
def uploaded_file():
    """Created file object in the database"""
    file_content = b'Test file content'
    file = SimpleUploadedFile('test_file.txt', file_content)
    return file
