from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
    if request.method == "GET":
        name = request.GET.get("name","")
        return HttpResponse("hello,%s!"%(name))
