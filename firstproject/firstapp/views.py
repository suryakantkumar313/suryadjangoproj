from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
	s='<h1> hello welcome to django project ....and it is to understand </h1>'
	return HttpResponse(s)
	



