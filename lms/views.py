from django.http import HttpResponse
from datetime import datetime
import random, string
from django.shortcuts import render
from .models import *


def info_student(request):
    student = Student.objects.all()
    return render(request,
                  'student.html',
                  {"student": student})

def mentor_info(request):
    mentor = Mentor.objects.all()
    return render(request,
                  'mentor.html',
                  {"mentor": mentor})

def task_info(request):
    task = Task.objects.all()
    return render(request,
                  'task.html',
                  {"task": task})

def visit_info(request):
    visit = Visit.objects.all()
    return render(request,
                  'visit.html',
                  {"visit": visit})



# def hello(request):
#     return HttpResponse("Привет это работа views+urls")
#
# def time(request):
#     time_now = datetime.now()
#     return HttpResponse(time_now)
#
# def hello(request):
#     name = request.GET.get('name', 'Гость')
#     return HttpResponse(f"Привет, {name}!")
#
# # def add(request):
# #     a = int(request.GET.get('a', 0))
# #     b = int(request.GET.get('b', 0))
# #     return HttpResponse(f"Сумма: {a + b}")
#
# def joke(request):
#     jokes = ["Байт — это укус программиста.", "Python — не только змея!", "Тостер — хлебный сервер."]
#     return HttpResponse(random.choice(jokes))
#
# def password(request):
#     pwd = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#     return HttpResponse(f"Твой новый пароль: {pwd}")
#
# def count(request):
#     word = request.GET.get('word', '')
#     return HttpResponse(f"В слове '{word}' — {len(word)} букв.")
#
#
# def hello_time(request):
#     hour = datetime.now().hour
#     if hour < 12:
#         msg = "Доброе утро!"
#     elif hour < 18:
#         msg = "Добрый день!"
#     else:
#         msg = "Добрый вечер!"
#     return HttpResponse(msg)
#
#
# def codecoin(request):
#     coins = random.randint(1, 100)
#     return HttpResponse(f"Ты заработал {coins} CodeCoin!")
#
# def languages(request):
#     langs = ["Python", "JavaScript", "C++", "Dart", "Kotlin"]
#     return HttpResponse('<br>'.join(langs))
#
# def next_lesson(request):
#     today = datetime.today()
#     next_day = today + datetime.time(days=7)
#     return HttpResponse(f"Следующее занятие: {next_day.strftime('%d.%m.%Y')}")