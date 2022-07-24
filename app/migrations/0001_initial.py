# Generated by Django 4.0.6 on 2022-07-24 01:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp4', 'mkv'])])),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('duration', models.FloatField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
