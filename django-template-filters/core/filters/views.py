from django.shortcuts import render
from .models import *
# date_of
# Create your views here.
def home(request):
    humanize_data={
        'num1':1,
        'num2':4500,
        'num3':1000000,
        'num4':'16-Nov-2023',
        'num5':'16-Nov-2023 16:30:00',
        'num6':8
    }
    data2={
        'num1':"lemon rice add slash",
        'num':"lemon,rice,add,slash",
        'num2':'lemon',
        'num3':"",
        'dict':{'lemon':1,'rice':2,'tej':0},
        'div':[11,2,3,4,5,6,7,8,9,0],
        'size':200023,

    }
    data=date_of.objects.all()
     
    return render(request,'index.html',{'humanize_data':humanize_data,'data':data,'data2':data2})