## student.py
from person import Person # import de la class person 

class Student(Person): # elle herite de person donc elle posede c attribu 
    def __init__(self, name, studentID, age): # dabord person 
        super().__init__(name, age) #
        self._studentID = studentID
        self._grades = []
    
    def add_grade(self, grade): # on ajoute une note a la liste grade 
        self._grades.append(grade)
    
    def get_average_grade(self): # 
        return sum(self._grades) / len(self._grades) if self._grades else 0

## undergraduate_student.py
from student import Student

class UndergraduateStudent(Student):
    pass

## graduate_student.py
from student import Student

class GraduateStudent(Student):
    def get_average_grade(self):
        return (super().get_average_grade() * 1.1)  # Example of polymorphism