from django.shortcuts import render
from django.contrib.auth.models import User

from ToDoList.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # user_list = User.objects.all()
    # print(user_list.query)
    # datas = [{"text":"哈哈哈哈哈","flag":True,"id":1}]
    if request.method == 'POST':
        Informations.objects.create(text=request.POST['data'], flag=0)
        print(request.POST['data'])
        return HttpResponseRedirect(reverse(index))
    datas = Informations.objects.all()
    print(datas.query)
    return render(request,"index.html",locals())

def delete(request):
    if request.method == 'GET':
        Informations.objects.filter(id=request.GET['no']).delete()
        print(request.GET['no'])
    print(request.method)
    return HttpResponseRedirect(reverse(index))
#
def edit(request):
    Informations.objects.filter(id=request.GET['no']).update(text=request.GET['data'])
    return HttpResponseRedirect(reverse(index))

def flag(request):
    if request.GET["flag"] == "True":
        Informations.objects.filter(id=request.GET['no']).update(flag=1)
        # pass
    else:
        Informations.objects.filter(id=request.GET['no']).update(flag=0)
        # pass
    return "no data"
    # return HttpResponseRedirect(reverse(index))
