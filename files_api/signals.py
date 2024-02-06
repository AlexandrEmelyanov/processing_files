import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import File
from .tasks import file_processing

logger = logging.getLogger(__name__)


@receiver(post_save, sender=File)
def created_file(sender: File, instance: File, created: bool, **kwargs: dict) -> None:
    """
    When a File object is created, it starts an async task (tasks.file_processing).
    Return -> None
    """
    if created:
        try:
            file = File.objects.get(id=instance.id)

        except File.DoesNotExist:
            logger.error(f'File #{instance.id} not found')

        else:
            file_id = file.id
            file_processing.delay(file_id)
            logger.info(f'File #{file_id} sent for processing')
