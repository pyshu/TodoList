from django.shortcuts import render
from django.contrib.auth.models import User

from ToDoList.models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    # user_list = User.objects.all()
    # print(user_list.query)
    if request.method == 'POST':
        Informations.objects.create(text=request.POST['data'], flag=0)
        print(request.POST['data'])
        return HttpResponseRedirect(reverse(index))
    else:
        page = request.GET.get('page')
    datas = Informations.objects.all()
    paginator = Paginator(datas, 5) # Show 5 contacts per page
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    print(datas.query)
    return render(request,"index.html",locals())

def delete(request):
    if request.method == 'GET':
        Informations.objects.filter(id=request.GET['no']).delete()
        print(request.GET['no'])
    print(request.method)
    return HttpResponseRedirect(reverse(index))

def edit(request):
    Informations.objects.filter(id=request.GET['no']).update(text=request.GET['data'])
    return HttpResponseRedirect(reverse(index))

def flag(request):
    try:
        if request.GET["flag"] == "True":
            Informations.objects.filter(id=request.GET['no']).update(flag=1)
        else:
            Informations.objects.filter(id=request.GET['no']).update(flag=0)
    except Exception as err:
        print(err)

    return HttpResponse(u'True')

