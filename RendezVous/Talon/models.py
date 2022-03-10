from django.db import models

from client.models import ClientProfile


class Talon(models.Model):
    user = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    order = models.AutoField(primary_key=True, verbose_name='порядковый номер')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return "00" + str(self.order)

    class Meta:
        verbose_name = 'Талон клиента'
        verbose_name_plural = 'Талоны клиентов'
