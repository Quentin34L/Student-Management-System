from student import Student, UndergraduateStudent, GraduateStudent
from course import Course

class Enrollment:
    def __init__(self):
        self.enrollments = {}
    
    def enroll_student(self, student, course):
        if course.course_code not in self.enrollments:
            self.enrollments[course.course_code] = []
        self.enrollments[course.course_code].append(student)
        course.register_student(student)
    
    def get_students_in_course(self, course_code):
        return [student.get_name() for student in self.enrollments.get(course_code, [])]

# Example Usage
if __name__ == "__main__":
    student1 = UndergraduateStudent("Alice", 101, 20, "Sophomore")
    student2 = GraduateStudent("Bob", 102, 25, "AI Research")
    
    course1 = Course("Math", "MATH101", 3)
    
    enrollment = Enrollment()
    enrollment.enroll_student(student1, course1)
    enrollment.enroll_student(student2, course1)
    
    print("Students in MATH101:", enrollment.get_students_in_course("MATH101"))