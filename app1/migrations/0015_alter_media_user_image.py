# Generated by Django 5.1.1 on 2024-10-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='user_image',
            field=models.ImageField(upload_to='image1/'),
        ),
    ]