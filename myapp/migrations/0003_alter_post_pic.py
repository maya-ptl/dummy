# Generated by Django 4.1.3 on 2022-11-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.FileField(upload_to='image/'),
        ),
    ]
