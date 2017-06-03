from django.shortcuts import render
from django.core.paginator import Paginator,Page
from hashlib import sha1
from models import Entry

# Create your views here.

def index(request):
    """"""
    return render(request, "booktest/index.html")

def register(request):
    """"""
    return render(request, "booktest/register.html")

def login(request):
    """"""
    dict = request.GET # "user", "upassword", "postbox"]
    user_name = dict.get("user_name")
    pwd = dict.get("pwd")
    cpwd = dict.get("cpwd")
    email = dict.get("email")
    if cpwd != pwd:
        return render(request, "booktest/register.html")

    s1 = sha1()
    s1.update(pwd)
    upwd3 = s1.hexdigest()

    user = Entry()#["user", "upassword", "postbox"]
    user.user = user_name
    user.upassword = pwd
    user.postbox = email
    user.save()
    return render(request, "booktest/login.html")

def index_2(request):
    """"""





























