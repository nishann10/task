# Generated by Django 5.1.1 on 2024-10-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auther_book1'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('project_title', models.TextField()),
            ],
        ),
    ]
