# Generated by Django 5.0.2 on 2024-05-01 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_mail_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
