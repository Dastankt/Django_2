from django.http import HttpResponse
from datetime import datetime
import random, string
from django.shortcuts import render
from .models import *

from django.shortcuts import redirect


def info_student(request):
    if request.method == 'POST':
        # Получаем данные из формы
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        avatar = request.FILES.get('avatar')

        # Создаем запись в базе
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            avatar=avatar
        )
        return redirect('student')  # Перенаправляем на страницу списка

    student = Student.objects.all()
    return render(request, 'student.html', {"student": student})

from django.shortcuts import render, redirect
from .models import Student, Mentor, Task, Visit


def dashboard(request):
    context = {
        "st_count": Student.objects.count(),
        "m_count": Mentor.objects.count(),
        "tasks_done": Task.objects.filter(is_completed=True).count(),
        "student_list": Student.objects.all(),
        "mentor_list": Mentor.objects.all(),  # Для формы добавления менторов
    }
    return render(request, 'index.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule, Mentor


def schedule_view(request):
    # ЛОГИКА ДОБАВЛЕНИЯ
    if request.method == 'POST' and 'add_schedule' in request.POST:
        day = request.POST.get('day')
        time = request.POST.get('time')
        subject = request.POST.get('subject')
        mentor_id = request.POST.get('mentor')

        if day and time and subject and mentor_id:
            mentor = get_object_or_404(Mentor, id=mentor_id)
            Schedule.objects.create(
                day=day,
                time=time,
                subject=subject,
                mentor=mentor
            )
        return redirect('schedule')

    # ЛОГИКА УДАЛЕНИЯ
    if request.method == 'POST' and 'delete_id' in request.POST:
        pk = request.POST.get('delete_id')
        item = get_object_or_404(Schedule, pk=pk)
        item.delete()
        return redirect('schedule')

    # ДАННЫЕ ДЛЯ СТРАНИЦЫ
    context = {
        'schedules': Schedule.objects.all().order_by('time'),
        'mentors': Mentor.objects.all(),
    }
    return render(request, 'schedule.html', context)


def mentor_info(request):
    if request.method == 'POST':
        Mentor.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            phone_number=request.POST.get('phone_number'),
            avatar=request.FILES.get('avatar'),
            is_mentor=True
        )
        return redirect('mentor')
    mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {"mentor": mentor})

def task_info(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        Task.objects.create(
            student=Student.objects.get(id=student_id),
            codecoin=request.POST.get('codecoin'),
            is_completed=request.POST.get('is_completed') == 'on'
        )
        return redirect('task')
    task = Task.objects.all()
    student = Student.objects.all()
    return render(request, 'task.html', {"task": task, "student": student})

def visit_info(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        Visit.objects.create(
            student=Student.objects.get(id=student_id),
            date=request.POST.get('date'),
            is_visited=request.POST.get('is_visited') == 'on'
        )
        return redirect('visit')
    visit = Visit.objects.all()
    student = Student.objects.all()
    return render(request, 'visit.html', {"visit": visit, "student": student})

def dashboard(request):
    # Эта функция для главной страницы
    context = {
        "st_count": Student.objects.count(),
        "m_count": Mentor.objects.count(),
        "tasks_done": Task.objects.count(),
    }
    return render(request, 'index.html', context)

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