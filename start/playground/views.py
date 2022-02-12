import http
from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    x = 1
    y = 2
    return HttpResponse("hello world palms")

def hello(request):
    return render(request,'hello/hello.html')

def more_html(request):
    return render(request, 'hello/more.html', {'name': 'derrick okinda '})