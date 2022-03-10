# Generated by Django 4.0.3 on 2022-03-09 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talon',
            fields=[
                ('order', models.AutoField(primary_key=True, serialize=False, verbose_name='порядковый номер')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.clientprofile')),
            ],
            options={
                'verbose_name': 'Талон клиента',
                'verbose_name_plural': 'Талоны клиентов',
            },
        ),
    ]