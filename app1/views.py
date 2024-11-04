from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
    ab=task.objects.get(title=name) 
    if request.method == 'POST':
        title1=request.POST.get('title_name')
        description1=request.POST.get('description_name')
        completed1=request.POST.get('completed_name')
        created1=request.POST.get('created_name')
        ab.title=title1
        ab.description=description1
        ab.completed=completed1
        ab.created=created1
        ab.save()
        return redirect('aa')
    return render(request,"task_updated.html",{'a':ab})

def taskdelete(request,name):
    ab=task.objects.get(title=name)
    ab.delete()
    return redirect('aa')
def bookget(request):
    ab=book.objects.all()
    return render(request,"book_get.html",{'a':ab})
def bookadd(request):
    user2=user.objects.all()
    if request.method =='POST':
        bookid=request.POST.get('id')
        bookname=request.POST.get('name')
        book_obj=book()
        book_obj.book_id=bookid
        book_obj.book_naame=bookname
        book_obj.user1=user.objects.get(user_id=request.POST.get('user_id'))
        book_obj.save()
    return render(request,"book_add.html",{'a':user2})
def productadd(request):
    if request.method == 'POST':
        name1=request.POST.get('name')
        price1=request.POST.get('price')
        created1=request.POST.get('created')
        product_obj=product()
        product_obj.product_name=name1
        product_obj.product_price=price1
        product_obj.created_at=created1
        product_obj.save()
    return render(request,"product_add.html")
def productget(request):
    ab=product.objects.all()
    if request.method =='POST':
        bc=request.POST.get('search')
        m1=product.objects.filter(Q(product_name__icontains=bc))
        return render(request,"product_get.html",{'a':m1})
    return render(request,"product_get.html",{'a':ab})
def productupdate(request,name):
    ab=product.objects.filter(product_name=name)
    if request.method == 'POST':
        name1=request.POST.get('name')
        price1=request.POST.get('price')
        created1=request.POST.get('created')
        product_obj=product()
        product_obj.product_name=name1
        product_obj.product_price=price1
        product_obj.created_at=created1
        product_obj.save()
        return redirect('bb')
    return render(request,"product_update.html",{'a':ab})
def book1add(request):
    ab=auther.objects.all()
    if request.method == 'POST':
        title1=request.POST.get('book_title')
        auther2=auther.objects.get(auther_name=request.POST.get('authername'))
        published=request.POST.get('book_published')
        book1_obj=book1()
        book1_obj.title=title1
        book1_obj.auther1=auther2
        book1_obj.published_date=published
        book1_obj.save()
    return render(request,"book1_add.html",{'a':ab})  
def book1get(request):
    ab=book1.objects.all()
    return render(request,"book1_get.html",{'a':ab})
def book1delete(request,name):
    ab=book1.objects.get(title=name)
    ab.delete()
    return redirect('cc')
def getall(request):
    my=project.objects.all()
    return render(request,"proget.html",{'my':my})
def userprofiles(request):
    if request.method == 'POST':
        form1=userprofileform(request.POST)
        if form1.is_valid():
            form1.save()
    else:
        form1=userprofileform()
                
    return render(request,"user_profile.html")
def auther1add(request):
    if request.method == 'POST':
        authername=request.POST.get('auther_name')
        autherbio=request.POST.get('auther_bio')
        auther1_obj=auther1()
        auther1_obj.name=authername
        auther1_obj.bio=autherbio
        auther1_obj.save()
    return render(request,"auther1_add.html") 
def auther1get(request):
    ab=auther1.objects.all()
    return render(request,"auther1_get.html",{'a':ab})
def auther1update(request,id):
    ab=auther1.objects.filter(auther_id=id)
    if request.method == 'POST':
        authername=request.POST.get('auther_name')
        autherbio=request.POST.get('auther_bio')
        auther1_obj=auther1()
        auther1_obj.name=authername
        auther1_obj.bio=autherbio
        auther1_obj.save()
        return redirect('dd')
    return render(request,"auther1_update.html",{'a':ab})
def vehicletable(request):
    if request.method == 'POST':
        form=vehicleform(request.POST)
        if form.is_valid:
            form.save()
    else:
        form=vehicleform()
    return render(request,"vehicle.html",{'form':form}) 

def book2add(request):
    ab=auther1.objects.all()
    if request.method =='POST':
        booktitle=request.POST.get('book_title')
        published=request.POST.get('book_date')
        book2_obj=book2()
        book2_obj.title=booktitle
        book2_obj.published_date=published
        book2_obj.auth=auther1.objects.get(auther_id=request.POST.get('aut'))
        book2_obj.save()
    return render(request,"book2_add.html",{'a':ab})   

def toysfunction(request):
    if request.method == 'POST':
        form=toysform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=toysform()
    return render(request,"login.html",{'form':form})       
def loginfuction(request):
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        form=registrationform(request.POST)
        if form.is_valid:
            form.save()
    else:
        form=registrationform()
    return render(request,"registration.html",{'form':form})   

def houseadd(request):
    if request.method == 'POST':
        form=houseform(request.POST)
        if form.is_valid:
            form.save()
    else:
        form=houseform()
    return render(request,"house.html",{'form':form})                        

def mediaget(request):
    ab=media.objects.all()
    return render(request,"media1.html",{'a':ab})
def media_add(request):
    if request.method == 'POST':
        id1 = request.POST.get('id')
        name1 = request.POST.get('name')
        image1 = request.FILES.get('image')  # Handling file uploads
        media_obj = media()
        media_obj.user_id = id1
        media_obj.user_name = name1
        media_obj.user_image = image1  # Saving the uploaded image file
        media_obj.save()
        return redirect('ee')  # Redirecting after successful save
    return render(request, "media1add.html")

def mediafileadd(request):
    if request.method == 'POST':
        title1=request.POST.get('media_title')
        file1=request.FILES.get('media_image')
        description1=request.POST.get('media_description')
        mediafile_obj=mediafile()
        mediafile_obj.title=title1
        mediafile_obj.file=file1
        mediafile_obj.description=description1
        mediafile_obj.save()
        return redirect('ff')
    return render(request,"mediafile_add.html")
def mediafileget(request):
    ab=mediafile.objects.all()
    return render(request,"mediafile_get.html",{'a':ab})

def basepage(request):
    return render(request,"base.html")
def homepage(request):
    return render(request,"home.html")
def aboutpage(request):
    return render(request,"about.html")
def contactpage(request):
    return render(request,"contacts.html")
def base1page(request):
    return render(request,"base1.html")
def postlist(request):
    if request.method == 'POST':
        title1=request.POST.get('block_title')
        content1=request.POST.get('block_content')
        created1=request.POST.get('block_created')
        updated1=request.POST.get('block_updated')
        block_obj=block()
        block_obj.title=title1
        block_obj.content=content1
        block_obj.created=created1
        block_obj.updated=updated1
        block_obj.save()
        return redirect('gg')
    return render(request,"post_list.html")  
def postdetail(request):
    ab=block.objects.all()
    return render(request,"post_detail.html",{'a':ab})  
def blockselect(request,id):
    ab=block.objects.get(id=id)
    return render(request,"block_select.html",{'a':ab})

# user=User.objects.create_user(username="nichu1",password="1234")
# user.save()

def setpassword(request):
    user=User.objects.get(username="nichu1")
    user.set_password("12345")
    user.save()
def checkpassword(request):
    user=User.objects.get(username="nichu1")
    if user.check_password("1234"):
        return HttpResponse(f"user authenticated ssuccesfully! username: ={user.username}")
    else:
        return HttpResponse("incorrect password")
def log(request):
    user=User.objects.get(username='nichu1')

    # print(user.last_login)   
    # return HttpResponse("hi") 

    # user.is_staff=True
    # user.save()

    # user.is_superuser=True
    # user.save()
    
    # return HttpResponse("hui")

    # username1='nichu1'
    # password1='12345'
    # user=authenticate(username=username1,password=password1)
    # if user is not None:
    #     return HttpResponse("user succsefully login")
    # else:
    #     return HttpResponse("user not valid")

def studentcourseadd(request):
    ab=courses1.objects.all()
    if request.method == 'POST':
        first_name1=request.POST.get("f_name")
        last_name1=request.POST.get("l_name")
        email1=request.POST.get("e_mail")
        phone1=request.POST.get("phone_number")
        studentcourse_obj=student_course()
        studentcourse_obj.first_name=first_name1
        studentcourse_obj.last_name=last_name1
        studentcourse_obj.email=email1
        studentcourse_obj.phone=phone1
        studentcourse_obj.course=courses1.objects.get(id=request.POST.get("course1"))
        studentcourse_obj.save()
        return redirect('sc')
    return render(request,"studentcourse_add.html",{'a':ab})
def studentcourseget(request):
    ab=student_course.objects.all()
    return render(request,"studentcourse_get.html",{'a':ab})
def studentcourseupdate(request,id):
    ab=courses1.objects.all()
    bc=student_course.objects.get(id=id)
    if request.method == 'POST':
        first_name1=request.POST.get("f_name")
        last_name1=request.POST.get("l_name")
        email1=request.POST.get("e_mail")
        phone1=request.POST.get("phone_number")
        bc.first_name=first_name1
        bc.last_name=last_name1
        bc.email=email1
        bc.phone=phone1
        bc.course=courses1.objects.get(id=request.POST.get("course1"))
        bc.save()
        return redirect('sc')
    return render(request,"studentcourse_update.html",{'a1':ab,'a':bc})
def studentcoursedelete(request,id):
    ab=student_course.objects.get(id=id)
    ab.delete()
    return redirect('sc')
def courseget(request):
    ab=courses1.objects.all()
    return render(request,"course_get.html",{'a':ab})
def scfilter(request,id):
    bc=courses1.objects.get(id=id)
    ab=student_course.objects.filter(course=bc) 
    return render(request,"scdetail.html",{'a':ab})
def sectionlogin(request):
    if request.method == 'POST':
        user_name1=request.POST.get("username")
        user_password1=request.POST.get("password")
        user=section_login.objects.filter(user_name=user_name1,password=user_password1).first()
        if user is not None:
            request.session['user_id']=user.id
            request.session['user_name']=user.user_name
            return redirect("ss")
        else:
            return render(request,"section_login.html")
     

    return render(request,"section_login.html")
def sectionhome(request):
    return render(request,"section_home.html")
def sectionlogout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('sslogin')   
def login1login(request):
    if request.method == 'POST':
        form=login1form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=login1form()
    return render(request,"login1.html",{'form':form})            

def login1home(request):
    return render(request,"login1home.html")
def login1check(request):
    if request.method == 'POST':
        user_name1=request.POST.get('username')
        e_mail1=request.POST.get('email')
        password1=request.POST.get('password')
        print(user_name1)
        user=login1.objects.filter(user_name=user_name1,e_mail=e_mail1,password=password1).first()
        if user is not None:
            request.session['user_id']=user.id
            request.session['user_name']=user.user_name
            return redirect('login1sign')
        else:
            return render(request,"login1check.html")
    return render(request,"login1check.html")   
def login1logout(request):
    if 'user_id' is not None:
        del request.session['user_id']
        return redirect('login1check')

def login2registration(request):
    if request.method == 'POST':
        username1=request.POST.get('user_name')
        password1=request.POST.get('pass_word')
        login2_obj=login2()
        login2_obj.username=username1
        login2_obj.password=password1
        login2_obj.save()
    return render(request,"login2_registration.html")

def login2login(request):
    if request.method == 'POST':
        username1=request.POST.get('user_name')
        password1=request.POST.get('pass_word')
        user=login2.objects.filter(username=username1,password=password1).first()
        if user is not None:
            request.session['user_id']=user.id
            request.session['user_name']=user.username
            return redirect('login2home_n')
        else:
            return redirect('login2login_n')          
    return render(request,"login2_login.html")

def login2home(request):
    return render(request,"login2_home.html")

def login2logout(request):
    if 'user_id'is not None:
        del request.session['user_id']
        return redirect('login2login_n')
def footballmedias(request):
    ab=footballmedia.objects.all()
    return render(request,"football_media.html",{'user':ab})

def footballform(request):
    if request.method == 'POST':
        name1=request.POST.get('name')
        club1=request.POST.get('club')
        image1=request.FILES.get('image')
        footballmedia_obj=footballmedia()
        footballmedia_obj.name=name1
        footballmedia_obj.club=club1
        footballmedia_obj.image=image1
        footballmedia_obj.save()
        return redirect('mfootball')
    return render(request,"football_form.html")

                 

  

 





