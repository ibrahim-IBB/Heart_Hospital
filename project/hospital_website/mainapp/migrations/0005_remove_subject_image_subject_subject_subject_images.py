# Generated by Django 5.0.2 on 2024-03-08 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_subject_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject_image',
            name='subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_images',
            field=models.ManyToManyField(to='mainapp.subject_image'),
        ),
    ]
