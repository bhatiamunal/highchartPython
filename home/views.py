from django.shortcuts import render,HttpResponse
from home.models import Dashboard
from django.contrib import  messages
# Create your views here.
def index(req):
    context = {
        'variable': "this is send"
    }
    return render(req,'index.html',context)
def about(req):
    context = {
        'variable': "this is send"
    }
    return render(req,'index.html',context)
    #return HttpResponse("this is about page")
def database(req):
    context = {
        'variable': "this is send"
    }
    if req.method =="POST":
        name = req.POST.get('name')
        password = req.POST.get('password')
        dob = req.POST.get('dob')
        mob = req.POST.get('mob')
        email = req.POST.get('email')
        print(password)
        database = Dashboard(name=name,password=password,dob=dob,mob=mob,email=email)
        database.save()
        print(messages)
        messages.success(req,'Profile updated')

    return render(req,'database.html',context)
    #return HttpResponse("this is database page")
def table(req):
    context = {
        'variable': "this is send"
    }
    return render(req,'table.html',context)
    #return HttpResponse("this is table page")
def analyze(req):
    context = {
        'variable': "this is send"
    }
    return render(req,'charts.html',context)
    return HttpResponse("this is analyze page")
def dashboard(req):
    context = {
        'variable': "this is send"
    }
    return render(req,'dashboard.html',context)
    #return HttpResponse("this is dashboard page")
def setting(req):
    context = {
        'variable': "this is send"
    }
    return render(req,'index.html',context)
    #return HttpResponse("this is setting page")