from django.contrib import admin
from .models import UserInfo,UserType,ClassInfo,MajorInfo,Attendence
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['studentNum','username','nickname','cid','password',
                    'major','gender','age','phone','email','motto'
                    ]

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id','caption']


class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class MajorInfoAdmin(admin.ModelAdmin):
    list_display = ['id','name',]

class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['id','stu','date','cur_time','is_leave','state','detail']
admin.site.register(UserType,UserTypeAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(ClassInfo,ClassInfoAdmin)
admin.site.register(MajorInfo,MajorInfoAdmin)
admin.site.register(Attendence,AttendenceAdmin)
