# Generated by Django 5.0.2 on 2024-03-09 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_subject_subject_contnet'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='sub_subjects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.subject'),
        ),
    ]