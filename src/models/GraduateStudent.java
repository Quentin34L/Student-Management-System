package models;

public class GraduateStudent extends Student {
    public GraduateStudent(String name, int age, String studentID) {
        super(name, age, studentID);
    }

    @Override
    public double getAverageGrade() {
        return super.getAverageGrade() + 5; // Exemple d'ajustement des notes
    }
}
