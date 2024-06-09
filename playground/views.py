from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    #return HttpResponse('hello World') would be clear html response
    return render(request, 'hello.html')