## enrollment.py
from course import Course
from student import Student

class Enrollment:
    def __init__(self, student, course):
        self._student = student
        self._course = course
    
    def register(self):
        self._course.enroll_student(self._student)
