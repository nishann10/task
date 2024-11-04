from django.db import models
from django.contrib.auth.models import User

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
class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=20)
    def __str__(self):
        return self.user_name
class book(models.Model):
    book_id=models.IntegerField(primary_key=True)
    book_naame=models.CharField(max_length=20)
    user1=models.ForeignKey(user,on_delete=models.CASCADE)           
class product(models.Model):
    product_name=models.CharField(primary_key=True,max_length=20)
    product_price=models.IntegerField()
    created_at=models.DateField()

class auther(models.Model):
    auther_name=models.CharField(primary_key=True,max_length=20)
    auther_email=models.EmailField()
    def __str__(self):
        return self.auther_name
class book1(models.Model):
    title=models.CharField(primary_key=True,max_length=20)
    auther1=models.ForeignKey(auther,on_delete=models.CASCADE)
    published_date=models.DateField()

class project(models.Model):
    project_name=models.CharField(max_length=100,unique=True)
    project_title=models.TextField()

class userprofile(models.Model):
    username=models.CharField(unique=True,max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    age=models.IntegerField()

class auther1(models.Model):
    auther_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    bio=models.TextField()
    def __str__(self):
        return self.name
class book2(models.Model):
    book_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    published_date=models.DateField()
    auth=models.ForeignKey(auther1,on_delete=models.CASCADE)
class toys(models.Model):
    colour=models.CharField(max_length=100)
    price=models.IntegerField()    
class vehicle(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
class registrtation(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
class house(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()            
class media(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_image=models.ImageField(upload_to='image1/')    

class mediafile(models.Model):
    title=models.CharField(max_length=100)
    file=models.ImageField(upload_to='image1/')
    description=models.TextField()   
class block(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created=models.DateField()
    updated=models.DateField()

class courses1(models.Model):
    course_name=models.CharField(max_length=100)
    course_code=models.CharField(max_length=100)
    course_date=models.DateField()
    def __str__(self):
        return self.course_name  
class student_course(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100) 
    course=models.ForeignKey(courses1,on_delete=models.CASCADE)  
class section_login(models.Model):
    user_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)     
    
class login1(models.Model):
    user_name=models.CharField(max_length=100)
    e_mail=models.EmailField()
    password=models.CharField(max_length=100)
class login2(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.username  
class footballmedia(models.Model):
    name=models.CharField(max_length=100)
    club=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image1/')
    
class bookrole(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    auther=models.CharField(max_length=100)
    class Meta:
        permissions=[
            ('add_book','book add'),
            ('edit_book','book edit'),
            ('delete_book','book delete'),
            ('borrow_book','book borrow'),
        ]
    def __str__(self):
        return self.name 

class bookuser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll_choice=(
        ('librarian','as_librarian'),
        ('member','as_member'),
        ('guest','as_guest'),
    )
    role=models.CharField(max_length=100,choices=roll_choice)
        
