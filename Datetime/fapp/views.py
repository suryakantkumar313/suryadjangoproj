from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(request):
    msg='<h1> this is from first app </h1>'
    return HttpResponse(msg)