from django.db import models


class File(models.Model):
    file = models.FileField(verbose_name='File name', upload_to='files')
    uploaded_at = models.DateTimeField(verbose_name='File upload date', auto_now_add=True)
    processed = models.BooleanField(verbose_name='File processed', default=False)

    def __str__(self):
        return f'File #{self.id} uploaded {self.uploaded_at}'

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'
