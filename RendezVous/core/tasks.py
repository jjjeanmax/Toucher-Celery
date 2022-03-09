import time
from celery import shared_task

from django.core.mail import send_mail

from RendezVous.settings.email import EMAIL_HOST_USER


@shared_task
def async_send_email_task(email, message):
    "background task to send an email asynchronously"
    subject = 'Prenez Rendez-Vous'
    # message = 'Confirmez Votre Mail et Obtenez Votre Talon Pour Vous Rendre Belle!!'

    # time.sleep(5)
    return send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )
