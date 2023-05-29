from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.gate, name='gate'),
    path('login', views.login, name='login'),
    path('notfound', views.notfound, name='notfound'),
    path('register', views.register, name='register'),
    path('viewStudents', views.view_students, name='view_students'),
    path('EditStudent/<int:student_id>/', views.Edit_Students, name='Edit_students'),
    path('Assign/<int:student_id>/', views.department, name='department'),
    path('delete_student/', views.delete_student, name='delete_student'),
    path('addStudent', views.add_Students, name='add_Student'),
    path('deleteStudent/<int:id>/', views.delete_student, name='delete_student'),
    path('assignDepartment', views.assign_Department, name='assign_Department'),
    path('contact', views.contact, name='contact'),
    path('logout', views.logout, name='logout'),
    path('Rand', views.Rand, name='Rand'),
]
 
