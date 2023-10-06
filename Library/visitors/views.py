from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Welcome')

def visitors(request):
    return HttpResponse('Visitors')

def banned_visitors(request):
    return HttpResponse('Banned visitors')

def books(request):
    return HttpResponse('Books')
