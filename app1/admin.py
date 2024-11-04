from django.contrib import admin
from .models import *

# Register your models here.
class blog_admin(admin.ModelAdmin):
    list_display=('title','auther','created',)
    search_fields=('title',)
    list_filter=('created',)
class task_admin(admin.ModelAdmin):
    list_display=('title','completed','created',)
    list_filter=('completed',)
    search_fields=('title',)    

admin.site.register(blog,blog_admin)
admin.site.register(task,task_admin)
admin.site.register(user)
admin.site.register(book)
admin.site.register(product)
admin.site.register(auther)
admin.site.register(book1)
admin.site.register(project)
admin.site.register(auther1)
admin.site.register(book2)
admin.site.register(vehicle)
admin.site.register(registrtation)
admin.site.register(house)
admin.site.register(media)
admin.site.register(mediafile)
admin.site.register(block)
admin.site.register(courses1)
admin.site.register(student_course)
admin.site.register(section_login)
admin.site.register(login1)
admin.site.register(login2)
admin.site.register(footballmedia)
admin.site.register(bookrole)
admin.site.register(bookuser)

