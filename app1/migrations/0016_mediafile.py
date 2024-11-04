# Generated by Django 5.1.1 on 2024-10-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_media_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediafile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.ImageField(upload_to='image1/')),
                ('description', models.TextField()),
            ],
        ),
    ]
