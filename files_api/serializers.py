from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ('uploaded_at', 'processed')

    def get_uploaded_at(self, obj: File):
        return obj.uploaded_at.strftime('%d-%m-%Y %H:%M:%S')