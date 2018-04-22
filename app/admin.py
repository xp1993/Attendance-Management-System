from django.contrib import admin
from .models import UserInfo, UserType, ClassInfo, MajorInfo, Attendence, Notice, Leave, Exam, ExamContent


# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['studentNum', 'username', 'nickname', 'cid', 'password',
                    'major', 'gender', 'age', 'phone', 'email', 'motto'
                    ]


class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption']


class ClassInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class MajorInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


class AttendenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'stu', 'date', 'start_time', 'end_time', 'is_leave', 'duration', 'detail']


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'head', 'content', 'level']


class LeaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time', 'explain']


class ExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'point', 'detail']


class ExamContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date', 'state']


admin.site.register(UserType, UserTypeAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(MajorInfo, MajorInfoAdmin)
admin.site.register(Attendence, AttendenceAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Leave, LeaveAdmin)
admin.site.register(ExamContent, ExamContentAdmin)
admin.site.register(Exam, ExamAdmin)

