from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class UserType(models.Model):
    caption = models.CharField(max_length=10)

    def __str__(self):
        return self.caption


class ClassInfo(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class MajorInfo(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    # 创建用户模型，学号,密码，班级，姓名,昵称，专业,用户类型,电话，姓名,座右铭,邮件
    studentNum = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=64)
    username = models.CharField(max_length=15)
    cid = models.ForeignKey('ClassInfo', null=True)
    nickname = models.CharField(max_length=30, null=True)
    major = models.ForeignKey('MajorInfo', null=True)
    hobby = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    user_type = models.ForeignKey(to='UserType')
    gender = models.IntegerField(default=1)
    phone = models.CharField(max_length=11)
    motto = models.TextField(null=True)
    email = models.EmailField(null=False)

    def __str__(self):
        return self.username


class Attendence(models.Model):
    stu = models.ForeignKey('UserInfo')
    # cur_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    duration=models.DecimalField(max_digits = 5 , decimal_places = 2,default=0)
    date=models.DateField(default=datetime.now())
    # state=models.BooleanField(default=False)
    is_leave = models.BooleanField(default=False)
    detail = models.TextField(default='无')
    def __str__(self):
        return self.stu.username
