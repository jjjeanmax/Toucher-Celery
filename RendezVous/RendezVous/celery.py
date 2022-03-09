from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RendezVous.settings')

app = Celery('RendezVous')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     # Обновление данных при необходимости для каждого устройства
#     'check_needly_update_data_from_devices': {
#         'task': 'mqtt_client.tasks.check_needly_update_data_from_devices',
#         # Каждую 10 секунд
#         'schedule': 10,
#     },
# }


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
