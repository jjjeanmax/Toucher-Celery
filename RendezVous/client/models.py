import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ClientProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField(verbose_name='номер телефона', unique=True)
    email = models.EmailField(verbose_name='email', null=True, blank=True)
    email_confirmed = models.BooleanField(verbose_name='подтверждена ли почта', default=False)
    last_name = models.CharField(verbose_name='фамилия', max_length=255, blank=True, null=True)
    first_name = models.CharField(verbose_name='имя', max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='дата и время на Встречу')

    class Meta:
        verbose_name = 'профиль клиента'
        verbose_name_plural = 'профили клиентов'
        unique_together = ('email', 'phone_number',)

    def __str__(self):
        return str(self.phone_number)
