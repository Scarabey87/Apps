from django.shortcuts import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('Welcome')
#
#
# def visitors(request):
#     return HttpResponse('Visitors')
#
#
# def banned_visitors(request):
#     return HttpResponse('Banned visitors')
#
#
def books(request, name, genre):
     return HttpResponse(f"""
             <h2>О пользователе</h2>
             <p>Имя: {name}</p>
             <p>Возраст: {genre}</p>
     """)

def home(request):
    return render(request, 'main/home.html')
