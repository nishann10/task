# Generated by Django 5.1.1 on 2024-10-01 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
