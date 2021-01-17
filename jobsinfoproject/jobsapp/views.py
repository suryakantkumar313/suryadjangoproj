from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def patnajobs(request):
    msg='<h1> patna jobs information here... </h1>'
    return HttpResponse(msg)

def delhijobs(request):
    msg='<h1> delhi jobs information here... </h1>'
    return HttpResponse(msg)

def hydrabaadjobs(request):
    msg='<h1> hydrabaad jobs information here... </h1>'
    return HttpResponse(msg)

def punejobs(request):
    msg='<h1> pune jobs information here... </h1>'
    return HttpResponse(msg)

def mumbaijobs(request):
    msg='<h1> mumbai jobs information here... </h1>'
    return HttpResponse(msg)

def noidajobs(request):
    msg='<h1> noida jobs information here... </h1>'
    return HttpResponse(msg)