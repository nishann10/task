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


