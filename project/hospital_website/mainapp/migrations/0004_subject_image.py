# Generated by Django 5.0.2 on 2024-03-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_subject_subject_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/sub_images')),
                ('subject', models.ManyToManyField(to='mainapp.subject')),
            ],
        ),
    ]
