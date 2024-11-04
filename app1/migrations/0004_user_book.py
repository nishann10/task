# Generated by Django 5.1.1 on 2024-09-26 06:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('book_id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_naame', models.CharField(max_length=20)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.user')),
            ],
        ),
    ]