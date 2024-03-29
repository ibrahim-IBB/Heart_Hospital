# Generated by Django 5.0.2 on 2024-03-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_subject_main_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('report_content', models.TextField(default=' ')),
                ('image', models.ImageField(upload_to='images/reports/')),
            ],
        ),
        migrations.AlterField(
            model_name='subject',
            name='main_title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
