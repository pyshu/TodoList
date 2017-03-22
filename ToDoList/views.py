from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    user_list = User.objects.all()
    print(user_list.query)
    datas = [{"text":"哈哈哈哈哈","flag":True,"id":1}]
    return render(request,"index.html",locals())
