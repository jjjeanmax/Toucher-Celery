from celery import shared_task
from celery.backends.rpc import RPCBackend

from django.core.mail import send_mail

from RendezVous.settings.email import EMAIL_HOST_USER
from RendezVous.celery import app
from .pdf import render_to_pdf


@shared_task
def async_send_email_task(email, message):
    "background task to send an email asynchronously"
    subject = 'Prenez Rendez-Vous'

    return send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [email],
        fail_silently=False
    )


@app.task(backend=RPCBackend(app=app))
def async_render_to_pdf(template_src, context_dict={}):
    return render_to_pdf(template_src, context_dict=context_dict)
