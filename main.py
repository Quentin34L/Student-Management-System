## main.py

from student import Student
from graduate_student import GraduateStudent
from undergraduate_student import UndergraduateStudent
from course import Course
from enrollment import Enrollment

# Creating students
student1 = Student("Alice", "S001", 20)
student2 = Student("Bob", "S002", 22)

# Adding grades
student1.add_grade(90)
student1.add_grade(85)
student2.add_grade(78)
student2.add_grade(88)

# Creating courses
course1 = Course("Math", "M101", 3)
course2 = Course("Physics", "P102", 4)

# Enrolling students
enrollment1 = Enrollment(student1, course1)
enrollment1.register()
enrollment2 = Enrollment(student2, course1)
enrollment2.register()
enrollment3 = Enrollment(student1, course2)
enrollment3.register()

# Displaying information
print(f"Student: {student1.get_name()}, Average Grade: {student1.get_average_grade()}")
print(f"Student: {student2.get_name()}, Average Grade: {student2.get_average_grade()}")

print(f"Course: {course1._courseName}, Enrolled Students: {course1.get_enrolled_students()}")
print(f"Course: {course2._courseName}, Enrolled Students: {course2.get_enrolled_students()}")
