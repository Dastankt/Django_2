from django.http import HttpResponse
from datetime import datetime
import random, string
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Mentor, Task, Visit
from .forms import *
from .models import Schedule


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




def mentor_items(request):
    sort_by = request.GET.get('sort', 'id')
    items = Mentor.objects.all().order_by(sort_by)
    if request.method == "POST":
        form = MentorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = MentorForm()

    return render(request, 'add_mentor.html', {
        'items': items,
        'form': form
    })

def student_items(request):
    sort_by = request.GET.get('sort', 'id')
    items = Student.objects.all().order_by(sort_by)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {
        'items': items,
        'form': form
    })

def task_items(request):
    sort_by = request.GET.get('sort', 'id')
    items = Task.objects.all().order_by(sort_by)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = TaskForm()

    return render(request, 'add_task.html', {
        'items': items,
        'form': form
    })

def visit_items(request):
    sort_by = request.GET.get('sort', 'id')
    items = Visit.objects.all().order_by(sort_by)
    if request.method == "POST":
        form = VisitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = VisitForm()

    return render(request, 'add_visit.html', {
        'items': items,
        'form': form
    })

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