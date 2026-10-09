student = [  {
        "name": "Ahmed",
        "age": 20,
        "grades": [80, 90, 75]
    },
    {
        "name": "Sara",
        "age": 21,
        "grades": [95, 88, 92]
    }]
def show_students(student):
    for s in student:
        print(f"Name: {s['name']}, Age: {s['age']}, Grades: {s['grades']}")
print("Student Information:")
show_students(student)   

def add_student():
    student = {}
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grades =input("Enter student's grades separated by commas: ")
    grades_list = [int(grade.strip()) for grade in grades.split(',')] 
    student = {
        "name": name,
        "age": age,
        "grades": grades_list
    }    
    
    return student
while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        student = add_student()
        print("Student added successfully!")
    elif choice == '2':
        if 'student' in locals():
            print("Student Information:")
            print(f"Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")
        else:
            print("No student information available.")       