"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadd',views.blogadd),
    path('blogget',views.blogget,name='aa'),
    path('blogupdate/<str:name>',views.blogupdate),
    path('blogdelete/<str:title2>',views.blogdelete),
    path('taskadd',views.taskadd),
    path('taskget',views.taskget,name='aa'),
    path('taskupdated/<str:name>',views.taskupdated),
    path('taskdelete/<str:name>',views.taskdelete),
    path('bookget',views.bookget),
    path('bookadd',views.bookadd),
    path('productadd',views.productadd),
    path('productget',views.productget,name='bb'),
    path('productupd/<str:name>',views.productupdate),
    path('book1add',views.book1add),
    path('book1get',views.book1get,name='cc'),
    path('book1dlt/<str:name>',views.book1delete),
    path('getall',views.getall),
    path('userprofile',views.userprofiles),
    path('auther1add',views.auther1add),
    path('auther1get',views.auther1get,name='dd'),
    path('auther1upt/<int:id>',views.auther1update),
    path('book2add',views.book2add),
    path('toys',views.toysfunction),
    path('login',views.loginfuction),
    path('vehicle',views.vehicletable),
    path('register',views.register),
    path('house',views.houseadd),
    path('media',views.mediaget,name='ee'),
    path('mediaadd',views.media_add),
    path('mediafileadd',views.mediafileadd),
    path('mediafileget',views.mediafileget,name='ff'),
    path('base',views.basepage),
    path('home',views.homepage),
    path('about',views.aboutpage),
    path('contact',views.contactpage),
    path('base1',views.base1page,name='gg'),
    path('home1',views.postlist),
    path('about1',views.postdetail),
    path('select/<int:id>',views.blockselect),
    path('checkpassword',views.checkpassword),
    path('setpassword',views.setpassword),
    path('log',views.log),
    path('scadd',views.studentcourseadd),
    path('scget',views.studentcourseget,name='sc'),
    path('scupdate/<int:id>',views.studentcourseupdate),
    path('scdelete/<int:id>',views.studentcoursedelete),
    path('courseget',views.courseget,name='scget'),
    path('scdetail/<int:id>',views.scfilter),
    path('sectionlogin',views.sectionlogin,name='sslogin'),
    path('sectionhome',views.sectionhome,name='ss'),
    path('sectionlogout',views.sectionlogout,name='logout'),
    path('login1',views.login1login),
    path('login1home',views.login1home,name='login1sign'),
    path('login1check',views.login1check,name='login1check'),
    path('login1logout',views.login1logout,name='logoutlogout'),
    path('login2reg',views.login2registration),
    path('login2in',views.login2login,name='login2login_n'),
    path('login2home',views.login2home,name='login2home_n'),
    path('login2out',views.login2logout,name='login2out_n'),
    path('fmedia',views.footballmedias,name='mfootball'),
    path('footballadd',views.footballform),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
