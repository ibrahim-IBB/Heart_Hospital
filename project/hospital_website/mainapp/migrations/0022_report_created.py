# Generated by Django 5.0.2 on 2024-03-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_report_alter_subject_main_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
