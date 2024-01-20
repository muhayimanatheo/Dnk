from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def shop(request):
 selectData=Photos.objects.all()
 return render(request,"shop.html",{'data':selectData})