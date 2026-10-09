# Student Data Structure
students = {
    "Ahmed": [55, 75, 88, 90],
    "Rehab": [51, 60, 44, 70],
    "Mohamed": [50, 70, 50, 75],
    "Ali": [55, 75, 55, 80],
    "Sara": [55, 75, 55, 80],
    "Eman": [55, 75, 55, 80],
}


def calculate_grade(average):
    if average >= 85:
        return "Excellent"
    elif average >= 75:
        return "Very Good"
    elif average >= 65:
        return "Good"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"


# Header Printout
print(
    f"{'Name':<10} | {'Marks':<18} | {'Total':<6} | {'Average':<8} | {'Grade':<10} | {'Status'}"
)
print("-" * 72)

# Report Processing Loop
for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)
    status = "Passed" if average >= 50 else "Failed"

    marks_str = str(marks)
    print(
        f"{name:<10} | {marks_str:<18} | {total:<6} | {average:<8.2f} | {grade:<10} | {status}"
    )