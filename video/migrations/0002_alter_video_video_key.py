# Generated by Django 3.2 on 2021-11-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_key',
            field=models.TextField(),
        ),
    ]
