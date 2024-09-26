from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    auther=models.CharField(max_length=100)
    created=models.DateField()
    updated=models.DateField()

class task(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    completed=models.BooleanField()
    created=models.DateField()    

    