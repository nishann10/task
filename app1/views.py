from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def blogadd(request):
    if request.method == 'POST':
        title1=request.POST.get('title')
        content1=request.POST.get('content')
        auther1=request.POST.get('auther')
        created1=request.POST.get('created')
        updated1=request.POST.get('updated')
        blog_obj=blog()
        blog_obj.title=title1
        blog_obj.content=content1
        blog_obj.auther=auther1
        blog_obj.created=created1
        blog_obj.updated=updated1
        blog_obj.save()
    return render(request,"blog_add.html")    
def blogget(request):
    blo=blog.objects.all()
    return render(request,"blog_get.html",{'a':blo})
def blogupdate(request,name):
    blo=blog.objects.filter(title=name)
    print(blo)
    if request.method == 'POST':
        title1=request.POST.get('title')
        content1=request.POST.get('content')
        auther1=request.POST.get('auther')
        created1=request.POST.get('created')
        updated1=request.POST.get('updated')
        print(title1,auther1,created1)
        blog_obj=blog()
        blog_obj.title=title1
        blog_obj.content=content1
        blog_obj.auther=auther1
        blog_obj.created=created1
        blog_obj.updated=updated1
        blog_obj.save()
        return redirect('aa')
    return render(request,"blog_update.html",{'a':blo})    
def blogdelete(request,title2):
    blo=blog.objects.get(title=title2)
    blo.delete()
    return redirect('aa')
def taskadd(request):
    if request.method == 'POST':
        title1=request.POST.get('title_name')
        description1=request.POST.get('description_name')
        completed1=request.POST.get('completed_name')
        created1=request.POST.get('created_name')
        task1=task()
        task1.title=title1
        task1.description=description1
        task1.completed=completed1
        task1.created=created1
        task1.save()
    return render(request,"task_add.html")
def taskget(request):
    ab=task.objects.all()
    return render(request,"task_get.html",{'a':ab})
def taskupdated(request,name):
    ab=task.objects.filter(title=name) 
    if request.method == 'POST':
        title1=request.POST.get('title_name')
        description1=request.POST.get('description_name')
        completed1=request.POST.get('completed_name')
        created1=request.POST.get('created_name')
        task1=task()
        task1.title=title1
        task1.description=description1
        task1.completed=completed1
        task1.created=created1
        task1.save()
        return redirect('aa')
    return render(request,"task_updated.html",{'a':ab})

def taskdelete(request,name):
    ab=task.objects.get(title=name)
    ab.delete()
    return redirect('aa')
        
