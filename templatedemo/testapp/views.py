from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

def profile(request):
    return render(request,'testapp/profile.html')









'''
def hello(request):
    date=datetime.datetime.now()
    name='surya'
    msg=''
    h=int(date.strftime('%H'))
    if h<12:
        msg='good morning'
    elif h<16:
        msg='afternoon'
    else:
        msg='good night'
    my_dict={'date':date,'name':name,'msg':msg}
    return render(request,'testapp/home.html',context=my_dict)
'''