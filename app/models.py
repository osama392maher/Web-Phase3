from django.db import models


# Create your models here.
class User(models.Model):

    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'User: {self.username} : {self.password}'

class Student(models.Model):

    name = models.CharField(max_length=50)
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    level = models.IntegerField()
    status = models.CharField(max_length=10)
    date = models.DateField()
    gpa = models.FloatField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}: {self.id}: "
    


        







