package main;
import models.*;

public class StudentManagementSystem {
    public static void main(String[] args) {
        Student s1 = new UndergraduateStudent("Alice", 20, "S001");
        Student s2 = new GraduateStudent("Bob", 25, "S002");

        s1.addGrade(85);
        s1.addGrade(90);
        s2.addGrade(80);
        s2.addGrade(70);

        Course course = new Course("Java Programming", "CS101", 3);

        Enrollment e1 = new Enrollment(s1, course);
        Enrollment e2 = new Enrollment(s2, course);

        e1.register();
        e2.register();

        System.out.println("Students enrolled in " + course.getEnrolledStudents().size() + " courses.");
        System.out.println(s1.getName() + " Average Grade: " + s1.getAverageGrade());
        System.out.println(s2.getName() + " Average Grade: " + s2.getAverageGrade());
    }
}
