# Generated by Django 5.1.1 on 2024-10-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_house'),
    ]

    operations = [
        migrations.CreateModel(
            name='media',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_image', models.ImageField(upload_to='', verbose_name='upload_to=image1/')),
            ],
        ),
    ]
