from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import User
from .models import Student

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
    students = Student.objects.all()
    return render(request, 'pages/view_Students.html', {'students': students})


def Edit_Students(request):
    return render(request, 'pages/EditStudentsPage.html')


def department(request):
    return render(request, 'pages/Department.html')


def contact(request):
    return render(request, 'pages/contact.html')


def assign_Department(request):
    return render(request, 'pages/Assign_Department.html')


def add_Students(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('id')
        level = request.POST.get('level')
        status = request.POST.get('status')
        date_of_birth = request.POST.get('date')
        department = request.POST.get('de')
        gpa = request.POST.get('gpa')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')

        student = Student(
            name=name,
            id=student_id,
            level=level,
            date=date_of_birth,
            department=department,
            gpa=gpa,
            email=email,
            gender=gender,
            phone=phone
        )

        student.save()

        return redirect('view_students')

    return render(request, 'pages/add_student.html')

