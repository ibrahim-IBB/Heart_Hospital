# Generated by Django 5.0.2 on 2024-03-20 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_alter_testing_sub_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='sub_subjects',
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_subjects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.subject'),
        ),
    ]
