from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import User
from .models import Student

from django.contrib.auth.forms import UserCreationForm


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
    return redirect('login')
    

