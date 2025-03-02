package models;
import java.util.*;

public class Student extends Person {
    private String studentID;
    private List<Double> grades;

    public Student(String name, int age, String studentID) {
        super(name, age);
        this.studentID = studentID;
        this.grades = new ArrayList<>();
    }

    public String getStudentID() { return studentID; }

    public void addGrade(double grade) {
        grades.add(grade);
    }

    public double getAverageGrade() {
        if (grades.isEmpty()) return 0;
        double sum = 0;
        for (double grade : grades) {
            sum += grade;
        }
        return sum / grades.size();
    }
}
