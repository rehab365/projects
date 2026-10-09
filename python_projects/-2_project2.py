a = input("Enter first number:")
operator =input("+ or - or * or /:")
b = input("Enter second number:")
if operator == "+":
   print(int(a)+int(b))
elif operator=="-":
   print(int(a)-int(b))
elif operator == "*":
   print(int(a)*int(b))
elif operator == "/":
   print(int(a)/int(b)) 
else:
    print("Invalid operator or character")    
print("========================")
print("      CALCULATOR")
print("========================")
choice = input("Enter your choice (1-4): ")
if choice == "1":
    add = int(input("a")) + int(input("b"))
    print(add)
elif choice == "2":
    subtract = int(input("a")) - int(input("b"))
    print(subtract)
elif choice == "3":
    multiply = int(input("a")) * int(input("b"))
    print(multiply) 
elif choice == "4":
    num1 = int(input("a"))
    num2 = int(input("b"))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        divide = num1 / num2
        print(divide)
else:
    print("Invalid choice. Please select a valid option (1-4).")

while True:
    answer = input("Do you want to continue? (yes/no): ")
    if answer.lower() == "yes":
        a = input("Enter first number:")
        operator =input("+ or - or * or /:")
        b = input("Enter second number:")
        if operator == "+":
            print(int(a)+int(b))
        elif operator=="-":
            print(int(a)-int(b))
        elif operator == "*":
            print(int(a)*int(b))
        elif operator == "/":
            print(int(a)/int(b)) 
        else:
            print("Invalid operator or character")
    if answer.lower() == "no":
            break  

