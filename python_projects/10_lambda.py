# هذاكر اخر حبة بكرا
# comprise
def multipy_by_2(n):
    return 2 * n
print(multipy_by_2(3)) # too much process
x = lambda n:n*2 # js in one line 
print(x(5))
add = lambda a,b,c,d,e,f:a+b+c+d+e+f
print(add(1,5,9,6,7,4))
multiply  = lambda a,b :a*b
print(multiply(80,90))
print(multiply(20,50))
# ************ Lambda with zero Parameters ************
hello =lambda:"Hello linux!"
print(hello())
# def greet():
#     return "Hello Paxto!"
# ************ Lambda Can Return Any Expression ************
greet = lambda name: "Hello " + name
print(greet("Paxto"))
is_even = lambda n: n % 2 == 0
print(is_even(9))
is_odd = lambda n: n % 2 != 0
print(is_odd(9))
length = lambda text: len(text)
# print(length("Python"))

maximum = lambda a, b: max(a, b)
print(maximum(10, 20))

# ************ Lambda + max() / min() ************
students = [
    {"name": "Ali", "marks": 85},
    {"name": "Ahmed", "marks": 92},
    {"name": "Bilal", "marks": 78}
]

# def get_marks(student):
#     return student["marks"]

# def maximum_marks(students):
#     return max(students, key=get_marks)

# print(maximum_marks(students))


top_student = max(
    students,
    key=lambda student: student["marks"]
)
print(top_student)
