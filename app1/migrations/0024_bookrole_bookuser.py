# Generated by Django 5.1.1 on 2024-11-01 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_footballmedia'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bookrole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('auther', models.CharField(max_length=100)),
            ],
            options={
                'permissions': [('add_book', 'book add'), ('edit_book', 'book edit'), ('delete_book', 'book delete'), ('borrow_book', 'book borrow')],
            },
        ),
        migrations.CreateModel(
            name='bookuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('librarian', 'as_librarian'), ('member', 'as_member'), ('guest', 'as_guest')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]