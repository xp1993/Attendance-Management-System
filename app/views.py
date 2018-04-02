from django.shortcuts import render, HttpResponse, redirect
from .forms import loginForm
from django.contrib.auth import authenticate, login
from .api import check_login, check_cookie, get_all_major, get_all_class, get_all_type
from .models import MajorInfo, UserType, UserInfo, ClassInfo
# django自带加密解密库
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json


# Create your views here.

# 首页
def index(request):
    return render(request, 'manage.html')


# 登录页面
@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        m1 = hashlib.sha1()
        m1.update(password.encode('utf8'))
        password = m1.hexdigest()
        print('密码:', password)
        if check_login(email, password):
            response = redirect('/index/')
            response.set_cookie('qwer', email, 3600)
            response.set_cookie('asdf', password, 3600)
            return response
            # return HttpResponse('登录成功')
        else:
            return render(request, 'page-login.html', {'error_msg': '账号或密码错误请重新输入'})
    else:
        (flag, rank) = check_cookie(request)
        print('flag', flag)
        if flag:
            return redirect('/index/')
        return render(request, 'page-login.html', {'error_msg': ''})


# 注册页面
@csrf_exempt
def register(request):
    if request.method == 'POST':
        if request.is_ajax():

            stu_num_v = request.POST.get('stu_num_verify')
            if UserInfo.objects.filter(studentNum=stu_num_v):
                ret = {'valid': False}
            else:
                ret = {'valid': True}

            return HttpResponse(json.dumps(ret))

    else:
        return render(request, 'register.html')


def check(request):
    (flag, rank) = check_cookie(request)
    print('flag', flag)
    if flag:
        return render(request, 'check.html', {'user': rank})

    return render(request, 'page-login.html', {'error_msg': ''})


# 注销登录
def logout(request):
    req = redirect('/login/')
    req.delete_cookie('asdf')
    req.delete_cookie('qwer')
    return req


# 注册验证
def register_verify(request):
    if request.method == 'POST':
        print('验证成功')
        username = request.POST.get('username')
        email = request.POST.get('email')
        stu_num = request.POST.get('stu_num')
        pwd = request.POST.get('password')
        m1 = hashlib.sha1()
        m1.update(pwd.encode('utf8'))
        pwd = m1.hexdigest()
        phone = request.POST.get('phone')
        a = UserInfo.objects.create(username=username, email=email, studentNum=stu_num, password=pwd,
                                    phone=phone, user_type_id=2)

        a.save()
        return HttpResponse('OK')


# 班级管理
def classManage(request):
    (flag, rank) = check_cookie(request)
    print('flag', flag)
    if flag:
        if rank.user_type.caption == 'admin':
            class_list = ClassInfo.objects.all()

            return render(request, 'classManage.html', {'class_list': class_list})
        else:
            return render(request, 'class_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})


# 编辑班级
@csrf_exempt
def edit_class(request):
    (flag, rank) = check_cookie(request)
    print('flag', flag)
    if flag:
        if rank.user_type.caption == 'admin':
            if request.method == 'POST':
                pre_edit_id = request.POST.get('edit_id')
                class_name = request.POST.get('edit_class_name')
                temp_flag = ClassInfo.objects.filter(name=class_name)
                print('pre_edit_id1', pre_edit_id)
                pre_obj = ClassInfo.objects.get(id=pre_edit_id)
                if not temp_flag and class_name:
                    pre_obj.name = class_name
                    pre_obj.save()
                return HttpResponse('班级修改成功')
            class_list = ClassInfo.objects.all()
            return render(request, 'classManage.html', {'class_list': class_list})
            # return HttpResponse('编辑班级')
        else:
            return render(request, 'class_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})


# 添加班级
@csrf_exempt
def add_class(request):
    # print('进来了')
    if request.method == 'POST':
        # print('这是post')
        add_class_name = request.POST.get('add_class_name')
        flag = ClassInfo.objects.filter(name=add_class_name)
        if flag:
            pass
            # print('已有数据，不处理')
        else:
            if add_class_name:
                ClassInfo.objects.create(name=add_class_name).save()

        return HttpResponse('添加班级成功')


# 删除班级
def delete_class(request):
    (flag, rank) = check_cookie(request)
    print('flag', flag)
    if flag:
        if rank.user_type.caption == 'admin':
            # class_list=ClassInfo.objects.all()
            delete_id = request.GET.get('delete_id')
            ClassInfo.objects.filter(id=delete_id).delete()
            return redirect('/classManage/')
        else:
            return render(request, 'class_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})


# 专业管理
def majorManage(request):
    (flag, rank) = check_cookie(request)
    if flag:
        if rank.user_type.caption == 'admin':
            major_list = MajorInfo.objects.all()

            return render(request, 'major_manage.html', {'major_list': major_list})
        else:
            return render(request, 'major_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})


# 添加专业
@csrf_exempt
def add_major(request):
    (flag, rank) = check_cookie(request)
    if flag:
        if rank.user_type.caption == 'admin':
            major_list = MajorInfo.objects.all()
            if request.method == 'POST':

                add_major_name = request.POST.get('add_major_name')
                print(add_major_name)
                if not MajorInfo.objects.filter(name=add_major_name):
                    new_major = MajorInfo.objects.create(name=add_major_name)
                    new_major.save()
                return HttpResponse('专业添加成功')

            return render(request, 'major_manage.html', {'major_list': major_list})
        else:
            return render(request, 'major_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})

#删除专业
def delete_major(request):
    (flag, rank) = check_cookie(request)
    if flag:
        if rank.user_type.caption == 'admin':
            major_list = MajorInfo.objects.all()
            delete_major_id=request.GET.get('delete_id')
            MajorInfo.objects.get(id=delete_major_id).delete()
            return render(request, 'major_manage.html', {'major_list': major_list})
        else:
            return render(request, 'major_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})

#编辑专业
@csrf_exempt
def edit_major(request):
    (flag, rank) = check_cookie(request)
    if flag:
        if rank.user_type.caption == 'admin':
            major_list = MajorInfo.objects.all()
            edit_major_id=request.POST.get('edit_major_id')
            edit_major_name=request.POST.get('edit_major_name')
            print(edit_major_id)
            print(edit_major_name)
            if not MajorInfo.objects.filter(name=edit_major_name):
                change_obj=MajorInfo.objects.get(id=edit_major_id)
                change_obj.name=edit_major_name
                change_obj.save()
            return HttpResponse('专业修改成功')

        else:
            return render(request, 'major_manage_denied.html')
    else:
        return render(request, 'page-login.html', {'error_msg': ''})


def member_manage(request):
    pass