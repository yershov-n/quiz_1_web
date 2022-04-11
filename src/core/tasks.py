from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.management import call_command

logger = get_task_logger(__name__)


@shared_task
def simple_task():
    logger.info(">>>>> THE SIMPLE TASK JUST RUN <<<<<")


@shared_task
def send_email_report():
    call_command('email_report')


@shared_task
def send_welcome_email():
    call_command('welcome_email')
