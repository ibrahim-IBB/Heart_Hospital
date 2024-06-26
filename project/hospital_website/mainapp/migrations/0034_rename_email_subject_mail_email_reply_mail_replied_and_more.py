# Generated by Django 5.0.2 on 2024-04-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_alter_mail_email_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mail',
            old_name='email_subject',
            new_name='email_reply',
        ),
        migrations.AddField(
            model_name='mail',
            name='replied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mail',
            name='user_visible',
            field=models.BooleanField(default=True),
        ),
    ]
