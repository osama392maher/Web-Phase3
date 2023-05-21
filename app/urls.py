from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.gate, name='gate'),
    path('login', views.login, name='login'),
    path('notfound', views.notfound, name='notfound'),
    path('register', views.register, name='register'),
    path('viewStudents', views.view_students, name='view_students'),
    path('EditStudent', views.Edit_Students, name='Edit_students'),
    path('addStudent', views.add_Students, name='add_Student'),
    path('assignDepartment', views.assign_Department, name='assign_Department'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='department'),
]
 
