from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def gate(request):
    return render(request, 'pages/gate.html')

def login(request):
    return render(request, 'pages/login.html')

def notfound(request):
    return render(request, 'pages/notfound.html')

def register(request):
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