# Generated by Django 5.1.1 on 2024-10-02 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auther1_book2'),
    ]

    operations = [
        migrations.CreateModel(
            name='toys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
