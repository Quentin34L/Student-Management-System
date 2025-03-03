package models;
import java.util.*;

public class Course {
    private String courseName;
    private String courseCode;
    private int creditHours;
    private List<Student> students;

    public Course(String courseName, String courseCode, int creditHours) {
        this.courseName = courseName;
        this.courseCode = courseCode;
        this.creditHours = creditHours;
        this.students = new ArrayList<>();
    }

    public void enrollStudent(Student student) {
        students.add(student);
    }

    public List<Student> getEnrolledStudents() {
        return students;
    }
}
    