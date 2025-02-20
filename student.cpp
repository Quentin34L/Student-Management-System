#ifndef STUDENT_H
#define STUDENT_H

#include <iostream>
#include <vector>
using namespace std; // la bibliotheque de goat 

class Student {
private:
    string name; // Nom de l'étudiant
    int studentID; // Numéro d’identification unique
    int age; // Âge de l’étudiant
    vector<double> grades; // Liste des notes obtenues

public:
    // Constructeur
    Student(string name, int id, int age);

    // Méthodes
    void addGrade(double grade); // Ajoute une note à l'étudiant
    double getAverageGrade(); // Retourne la moyenne des notes
    void display(); // Affiche les infos de l'étudiant
    int getID(); // Retourne l'ID de l'étudiant
};

#endif


