from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at', 'processed')
    search_fields = ('uploaded_at', 'file')
    ordering = ('-uploaded_at',)
    list_per_page = 10
    list_filter = ('processed', 'uploaded_at')
    readonly_fields = ('uploaded_at', 'processed')