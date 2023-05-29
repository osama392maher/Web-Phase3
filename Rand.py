import random
import string
from datetime import date
from app.models import Student
from django.utils.crypto import get_random_string
import os
import django

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Student


def add_10_students():
    for _ in range(10):
        # Generate random data for each student
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        student_id = ''.join(random.choices(string.ascii_uppercase, k=6))
        level = 3
        status = 'Active'
        birth_date = date(year=2000, month=1, day=1)  # Replace with appropriate birth dates
        gpa = 3.5
        gender = 'Male'
        department = 'CS'
        email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + '@example.com'
        phone = '0123456789'

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

add_10_students()
