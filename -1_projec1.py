students=[
    {
        "name": "Ahmed",
        "age": 20,
        "grades": [80, 90, 75]
    },
    { 
      "name": "Sara",
      "age": 21,
      "grades": [95, 88, 92]
    },
    {
        "name": "Mohamed",
        "age": 22,
        "grades": [85, 90, 65]
    }
]

def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades = input("Enter student's grades separated by commas: ")
    grades_list = [int(grade.strip()) for grade in grades.split(',')]
    student = {
        "name": name,
        "age": age,
        "grades": grades_list
    }
    students.append(student)
    print("Student added successfully!")
def show_students():
    if not students:
        print("No student found. ")
        return

    
    print("\n===== Student Information =====")
    for student in students:
        print(f"Name: {student['name']}")
        print(f" Age: {student['age']}") 
        print(f"Grades: {student['grades']}")
        print()
def search_student():
    name = input("Enter your name to seaarch: ")   


    for student in students:
        if student['name'].lower() == name.lower():
            print("\nStudent found!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grades: {student['grades']}")
            return
    print("Student not found.")


def calculate_average_grade():
    name = input("Enter student's name to calculate average grade: ")


    for student in students:
        if student['name'].lower() == name.lower():
           average = sum(student["grades"]) / len(student["grades"])
           print(f"{student['name']}'s average: {average:.2f}")
           return 
        print("Student not found.")

def find_highest_student():
    if not students:
        print("No student found.")
        return
    highest_student = -1
    top_student = ""
    for student in students:
        student_highest = max(student["grades"])
        if student_highest > highest_student:
            highest_student = student_highest
            top_student = student["name"]
    print(f"The student with the highest grade is {top_student} with a grade of {highest_student}.")
def update_student():
    name = input("Enter the name of the student to update: ")
    for student in students:
        if student['name'].lower() == name.lower():
            new_grades = input(
           "Enter the new grades separated by commas: "
             )             
            new_grades_list = [ int(grade.strip())for grade in new_grades.split(",")]
            student['grades'] = new_grades_list
            print(f"{student['name']}'s grades have been updated to {student['grades']}.")
            return
    print("Student not found.")
def delete_student():
    name = input("Enter student's name: ")

    for student in students:
        if student["name"].lower() == name.lower():

            students.remove(student)

            print(f"Student {name} deleted.")
            return

    print("Student not found.")       
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Calculate Average Grade")
    print("5. Find Highest Student")
    print("6. Update Student Grades")
    print("7. Delete Student")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        calculate_average_grade()
    elif choice == '5':
        find_highest_student()
    elif choice == '6':
        update_student()
    elif choice == '7':
        delete_student()
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")     
            