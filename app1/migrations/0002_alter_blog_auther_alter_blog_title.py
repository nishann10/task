# Generated by Django 5.1.1 on 2024-09-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='auther',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
