import logging

from celery import shared_task

from .models import File

logger = logging.getLogger(__name__)


@shared_task
def file_processing(file_id) -> None:
    """
    The task is run from 'signals.py'.
    The task simulates the processing of a file. Based on the results, the 'processed' field is set to 'True'.
    Return -> None
    """

    try:
        file = File.objects.get(id=file_id)

    except File.DoesNotExist:
        logger.error(f'File #{file_id} not found')

    else:
        file.processed = True
        file.save()
        logger.info(f'The file #{file.id} has been successfully processed. Status changed to True')
