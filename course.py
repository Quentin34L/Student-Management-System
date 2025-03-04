## course.py
class Course:
    def __init__(self, courseName, courseCode, creditHours):
        self._courseName = courseName
        self._courseCode = courseCode
        self._creditHours = creditHours
        self._students = []
    
    def enroll_student(self, student):
        self._students.append(student)
    
    def get_enrolled_students(self):
        return [student.get_name() for student in self._students]
