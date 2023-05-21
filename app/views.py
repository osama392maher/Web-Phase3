from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import User

from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def gate(request):
    return render(request, 'pages/gate.html')


def login(request):
    return render(request, 'pages/login.html')


def notfound(request):
    return render(request, 'pages/notfound.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        model = User(username=username, password=password)
        model.save()
        return redirect('pages/add_student.html')
    else:
        return render(request, 'pages/Register.html')


def view_students(request):
    return render(request, 'pages/view_Students.html')


def Edit_Students(request):
    return render(request, 'pages/EditStudentsPage.html')


def department(request):
    return render(request, 'pages/Department.html')


def contact(request):
    return render(request, 'pages/contact.html')


def assign_Department(request):
    return render(request, 'pages/Assign_Department.html')


def add_Students(request):
    return render(request, 'pages/add_Student.html')
