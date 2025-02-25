class Course:
    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits
        self.students = []
    
    def register_student(self, student):
        self.students.append(student)
    
    def get_students(self):
        return [student.get_name() for student in self.students]