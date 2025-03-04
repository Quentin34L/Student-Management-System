## graduate_student.py
from student import Student

class GraduateStudent(Student):
    def get_average_grade(self):
        return (super().get_average_grade() * 1.1)  # Example of polymorphism