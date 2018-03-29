from .models import UserInfo,MajorInfo,ClassInfo,UserType


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