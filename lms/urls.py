from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('student/', views.info_student, name='student'),
    path('mentor/', views.mentor_info, name='mentor'),
    path('task/', views.task_info, name='task'),
    path('visit/', views.visit_info, name='visit'),
    path('', views.dashboard, name='home'),
    path('schedule/', views.schedule_view, name='schedule'),
    path('add_mentor/', views.mentor_items, name='mentor_items'),
    path('add_student/', views.student_items, name='student_items'),
    path('add_task/', views.task_items, name='task_items'),
    path('add_visit/', views.visit_items, name='visit_items')




    # path('hello/', views.hello, name='hello'),
    # path('time/', views.time, name='time'),
    # path('joke/', views.joke, name='joke'),
    # path('password/', views.password, name='password'),
    # path('count/', views.count, name='count'),
    # path('hello_time/', views.hello_time, name='hello_time'),
    # path('codecoin/', views.codecoin, name='codecoin'),
    # path('languages/', views.languages, name='languages'),
    # path('next_lesson/', views.next_lesson, name='next_lesson')
]