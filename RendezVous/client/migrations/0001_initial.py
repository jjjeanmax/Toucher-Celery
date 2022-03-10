# Generated by Django 4.0.3 on 2022-03-09 19:33

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='подтверждена ли почта')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='фамилия')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='имя')),
                ('created_at', models.DateTimeField(verbose_name='дата и время на Встречу')),
            ],
            options={
                'verbose_name': 'профиль клиента',
                'verbose_name_plural': 'профили клиентов',
            },
        ),
    ]
