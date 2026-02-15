from django.db import models


class Student(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    phone_number = models.IntegerField()
    avatar = models.ImageField(upload_to='media/')


class Mentor(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    phone_number = models.IntegerField()
    avatar = models.ImageField(upload_to='media/')
    is_mentor = models.BooleanField(default=True)


class Task(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    codecoin = models.IntegerField()
    is_completed = models.BooleanField(default=False)


class Visit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_visited = models.BooleanField(default=False)
    date = models.DateField()


class Schedule(models.Model):
    DAYS = [
        ('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СР', 'Среда'),
        ('ЧТ', 'Четверг'), ('ПТ', 'Пятница'), ('СБ', 'Суббота'),
    ]
    day = models.CharField(max_length=2, choices=DAYS)
    time = models.TimeField()
    subject = models.TextField(max_length=50)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day} | {self.subject}"