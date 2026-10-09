import json
class Student:
    def __init__(self , name , age , grades):
        self.name = name
        self.age = age
        self.grades = grades
    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrades: {self.grades}"
    def calculate_average(self):
        return sum(self.grades) / len(self.grades)
    def highest_grade(self):
        return max(self.grades)
   
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_students()
    def load_students(self):
        try:
            with open("students.json", "r") as file:
                students_data = json.load(file)
                for student_data in students_data:
                    student = Student(student_data["name"], student_data["age"], student_data["grades"])
                    self.students.append(student)
        except FileNotFoundError:
            print("No existing student data found. Starting with an empty list.")
        except json.JSONDecodeError:
            print("Error decoding JSON data. Starting with an empty list.")                    
    def add_student(self):
        name = input("Enter you name: ")
        age = input("Enter your age: ")
        try:
            age = int(age)
        except ValueError:
            print("Invalid age. Please enter a valid integer.")
            return    
        grades = input("Enter your grades separated by commas: ")
        try:
            grades_list = [int(grade.strip()) for grade in grades.split(',')]  
        except ValueError:
            print("Invalid grades. Please enter valid integers separated by commas.")
            return

        student = Student(name, age, grades_list)
        self.students.append(student)
        print("Student added successfully!")
    def show_students(self):
        if not self.students:
            print("No student found.")
            return
        print("\n===== Student Information =====")
        for student in self.students:
            print(student)
            print()
    def search_student(self,name):
        for student in self.students:
            if student.name.lower() == name.lower():
                print("\nStudent found!")
                print(student)
                return
        print("Student not found.")

file= open("students.json","r")
students = json.load(file)
file.close()