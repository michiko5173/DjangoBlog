from django.shortcuts import render

# Create your views here.
from cmdb.models import cmdb
from django.shortcuts import HttpResponse
from datetime import datetime
def home(request):
    post_list=cmdb.objects.all()
    return render(request,'home.html',{'post_list':post_list})
