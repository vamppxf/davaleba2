import random
from django.shortcuts import render

def get_random_students():
    students = []
    for _ in range(100):
        student = {
            'name': f'Name{random.randint(1, 100)}',
            'surname': f'Surname{random.randint(1, 100)}',
            'gpa': round(random.uniform(1.0, 4.0), 2),
            'course': random.randint(1, 4),
        }
        students.append(student)
    return students

def main_page_view(request):
    students = get_random_students()
    student = random.choice(students)
    return render(request, 'students/main_page.html', {'student': student})

def students_page_view(request):
    students = get_random_students()
    return render(request, 'students/students_page.html', {'students': students})
