# Generated by Django 5.0.2 on 2024-03-08 21:00

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_subject_subject_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_content',
            field=tinymce.models.HTMLField(),
        ),
    ]
