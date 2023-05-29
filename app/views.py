from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.decorators.http import require_POST
import random

from .models import User
from .models import Student

from django.contrib.auth.forms import UserCreationForm

import string
from datetime import date



# Create your views here.
def index(request):
    if 'current_user' not in request.session:
        return redirect('login')
    return render(request, 'pages/index.html')


def gate(request):
    return render(request, 'pages/gate.html')

def login(request):
    if request.method == "POST":

        request.session.flush()
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['current_user'] = username  # Store username in session
                print("Form submitted and login successful")
                return redirect('index')  # Redirect to 'index' URL
        except User.DoesNotExist:
            pass

        messages.error(request, "Invalid login, please try again")
        print("Form submitted, but login failed")
        return redirect('login')

    else:
        print("Form not submitted")
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
        return redirect('index')
    else:
        return render(request, 'pages/Register.html')


def view_students(request):
    if 'current_user' not in request.session:
        return redirect('login')
    students = Student.objects.all()
    return render(request, 'pages/view_Students.html', {'students': students})


def assign_Department(request):
    if 'current_user' not in request.session:
        return redirect('login')
    students = Student.objects.all()
    return render(request, 'pages/Assign_Department.html', {'students': students})


def department(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('notfound')
    
    if request.method == 'POST':
        # Update student data based on the form submission
        if student.level >= 3:
            student.department = request.POST.get('de')
            student.save()
            return redirect('assign_Department')
        else:
            error_message = "This action is only applicable for students of level over 3."
            return render(request, 'error.html', {'error_message': error_message})
    return render(request, 'pages/Department.html', {'student': student})


def Edit_Students(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('notfound')

    if request.method == 'POST':
        # Update student data based on the form submission
        student.name = request.POST.get('name')
        student.level = request.POST.get('level')
        student.status = request.POST.get('status')
        student.date = request.POST.get('date')
        student.department = request.POST.get('de')
        student.gpa = request.POST.get('gpa')
        student.email = request.POST.get('email')
        student.gender = request.POST.get('gender')
        student.phone = request.POST.get('phone')
        student.save()

        return redirect('view_students')
    else:
        if 'current_user' not in request.session:
            return redirect('login')
    # Render the template and pass the student data as context variables
    return render(request, 'pages/EditStudentsPage.html', {'student': student})


def delete_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return redirect('view_students') 
        except Student.DoesNotExist:
            return redirect('view_students')  
    else:
        if 'current_user' not in request.session:
            return redirect('login')
    return redirect('view_students')





def contact(request):
    return render(request, 'pages/contact.html')




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
            status=status,
            department=department,
            gpa=gpa,
            email=email,
            gender=gender,
            phone=phone
        )

        student.save()

        return redirect('view_students')
    else:
        if 'current_user' not in request.session:
            return redirect('login')

    return render(request, 'pages/add_student.html')


def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out")
    return redirect('login')

def Rand(request):
    #array of departments
    department_choices = ['NO', 'CS', 'IS', 'AI', 'DS', 'IT']
    status_choices = ['Active', 'Inactive']
    gender_choices = ['Male', 'Female']
    #array of names
    names = ['Ahmed', 'Mohamed', 'Ali', 'Omar', 'Mahmoud', 'Khaled', 'Hassan', 'Abdullah', 'Abdelrahman', 'Youssef', 'Amr', 'Yahia', 'Mostafa', 'Hussein', 'Ibrahim', 'Adham', 'Othman', 'Yehia']
    
    #email will be name.name@name
    #phone will be random 11 digits
    #gpa will be random float from 0 to 4
    #level will be random int from 1 to 4
    #date will be random date from 1990 to 2000
    #department will be random from array of departments
    #status will be random from array of status

  # Generate random data for each student
    name = random.choice(names)
    student_id = ''.join(random.choices(string.digits, k=6))
    level = random.randint(1, 4)
    status = random.choice(status_choices)
    birth_date = date(random.randint(1990, 2000), random.randint(1, 12), random.randint(1, 28))
    gpa = round(random.uniform(0, 4), 2)
    gender = random.choice(gender_choices)
    department = random.choice(department_choices)
    email = f'{name.lower()}.{name.lower()}@{name.lower()}'
    phone = ''.join(random.choices(string.digits, k=11))

    # Create a new student instance
    student = Student(
        name=name,
        id=student_id,
        level=level,
        status=status,
        date=birth_date,
        gpa=gpa,
        gender=gender,
        department=department,
        email=email,
        phone=phone
    )

    # Save the student to the database
    student.save()
    return redirect('view_students')
    

