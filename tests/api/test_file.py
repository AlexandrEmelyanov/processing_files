import pytest

from django.utils import timezone
from rest_framework import status

from files_api.models import File
from files_api.tasks import file_processing


@pytest.mark.django_db
class TestFileProcessing:
    """Test model and processing"""
    def test_file_create(self, uploaded_file):
        """Testing the creation of an object in the database directly"""
        file = File.objects.create(file=uploaded_file)

        file_from_db = File.objects.all().first()

        assert file.file.name == file_from_db.file
        assert file.uploaded_at <= timezone.now()
        assert not file.processed

    def test_file_processing(self, uploaded_file):
        """Testing file processing via task"""
        file = File.objects.create(file=uploaded_file)

        file_processing(file.id)
        file.refresh_from_db()

        assert file.processed


@pytest.mark.django_db
class TestFileView:
    """Test API"""
    def test_post_file(self, client, uploaded_file):
        """Testing post request to add and save a file on the server"""
        payload = {'file': uploaded_file}

        response = client.post('/api/v1/upload/', data=payload)
        data = response.data
        file_from_db = File.objects.all().first()

        assert response.status_code == status.HTTP_201_CREATED
        assert data['id'] == file_from_db.id

    def test_get_files(self, client, uploaded_file):
        """Testing a get request to get a list of all files"""
        File.objects.create(file=uploaded_file)

        response = client.get('/api/v1/files/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

    def test_get_file_detail(self, client, uploaded_file):
        """Testing a get request to retrieve a specific file"""
        file = File.objects.create(file=uploaded_file)

        response = client.get(f'/api/v1/files/{file.id}/')
        data = response.data

        assert response.status_code == status.HTTP_200_OK
        assert data['id'] == file.id
