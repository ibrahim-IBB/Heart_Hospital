# Generated by Django 5.0.2 on 2024-05-03 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_alter_subject_subject_contnet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_time', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=15)),
                ('job_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_contnet',
            field=models.TextField(default=' ', help_text='\ntext item:<br><br>\n      &lt;div class=&quot;text_item&quot;&gt;<br>\n         نص للتجربة<br>\n        &lt;/div&gt;       <br>   <br>                      \nmulti_image (اكثر من صورة):<br><br>\n          &lt;div class=&quot;multi_image_item&quot;&gt;<br>\n            &lt;img src=&quot;3&quot; alt=&quot;&quot;&gt;<br>\n            &lt;img src=&quot;2&quot; alt=&quot;&quot;&gt;<br>\n            &lt;img src=&quot;1&quot; alt=&quot;&quot;&gt;<br>\n        &lt;/div&gt;<br><br>\nimage_item (صورة واحدة):<br><br>\n                                     \n           &lt;div class=&quot;image_item&quot;&gt;<br>\n            &lt;img src=&quot;1&quot; alt=&quot;&quot;&gt;<br>\n        &lt;/div&gt;                           \n'),
        ),
    ]
