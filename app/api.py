from .models import UserInfo,MajorInfo,ClassInfo,UserType
from functools import wraps
from django.shortcuts import render
import json
import decimal
def check_cookie(request):
    d = request.COOKIES.keys()
    if "qwer" in d and "asdf" in d:
        email = request.COOKIES['qwer']
        password = request.COOKIES['asdf']
        select_user = UserInfo.objects.filter(email=email).filter(password=password)
        if len(select_user) == 0:
            return (False, -1)
        else:
            return (True, select_user[0])
    else:
        return (False, -1)


def is_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        (flag, rank) = check_cookie(request)
        if flag:
            return func(request, *args, **kwargs)
        else:
            return render(request, 'page-login.html', {'error_msg': ''})
    return inner


def check_login(email, password):
    select_user = UserInfo.objects.filter(email=email).filter(password=password)
    if len(select_user) == 0:
        return False
    else:
        return True

def get_all_major():

    return MajorInfo.objects.all()

def get_all_class():
    return  ClassInfo.objects.all()

def get_all_type():
    return  UserType.objects.all()

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,decimal.Decimal):
            return float(obj)
        return super(DecimalEncoder,self).default(obj)