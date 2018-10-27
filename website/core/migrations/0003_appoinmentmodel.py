# Generated by Django 2.1.2 on 2018-10-27 20:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181024_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppoinmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_name', models.CharField(max_length=30)),
                ('appoinment_email', models.CharField(max_length=30)),
                ('appoinment_date', models.CharField(max_length=30)),
                ('appoinment_phone', models.CharField(max_length=30)),
                ('appoinment_message', models.CharField(max_length=30)),
                ('appoinment_sent_date', models.DateTimeField(default=django.utils.timezone.now, max_length=35)),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
            },
        ),
    ]
