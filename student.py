class Student:
    def __init__(self, name, student_id, age):
        self.__name = name
        self.__student_id = student_id
        self.__age = age
        self.__grades = []
    
    def get_name(self):
        return self.__name
    
    def get_student_id(self):
        return self.__student_id
    
    def get_age(self):
        return self.__age
    
    def add_grade(self, grade):
        self.__grades.append(grade)
    
    def get_average_grade(self):
        return sum(self.__grades) / len(self.__grades) if self.__grades else 0

class UndergraduateStudent(Student):
    def __init__(self, name, student_id, age, year):
        super().__init__(name, student_id, age)
        self.year = year

class GraduateStudent(Student):
    def __init__(self, name, student_id, age, thesis_topic):
        super().__init__(name, student_id, age)
        self.thesis_topic = thesis_topic
