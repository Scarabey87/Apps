from django.shortcuts import HttpResponse
from django.shortcuts import render
import sqlite3, random, os, time, datetime

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

con = sqlite3.connect("db.sqlite.db")
cursor = con.cursor()

# # создаем таблицу people
# cursor.execute("""CREATE TABLE visitors
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 age INTEGER)
#             """)
# добавляем строку в таблицу people
# cursor.execute("INSERT INTO visitors (name, age) VALUES ('Tom', 38)")
# # выполняем транзакцию
# con.commit()
cursor.execute("SELECT * FROM visitors")
cmd = cursor.fetchall()
print(cmd)
# def p(cmd):
#     for i in cmd:
#         return f'{cmd[0][1]} {cmd[0][2]}'

a = datetime.date.today()
b = datetime.datetime.now()

def home(request):
    return render(request, 'main/home.html')

def common(request, name=None, time = None):
    return render(request, 'main/common.html', {"name": a, "time":b})


