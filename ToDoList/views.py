from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    datas = [{"text":"哈哈哈哈哈","flag":True,"id":1}]
    return render(request,"index.html",locals())
