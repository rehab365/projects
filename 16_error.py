# while True:
#    try:
#       number=int(input("Enter a number: "))
#       print(10/number)
#    except ValueError:
#       print("That's not a valid number")
#    except ZeroDivisionError:
#       print("Can't divide by Zero ")
# try:
#     file = open("data.txt")
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid number")
# finally:
#     file.close()
#     print("File closed — this always runs")
# try:
#     int("10")
# except ValueError as e:
#     print(f"Error occured:{e}")    
#else — Runs Only When Nothing Went Wrong
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a valid number")
# else:
#     print(f"Great, you entered {number}")
# def withdraw(balance, amount):
#     if amount > balance:
#         raise ValueError("Insufficient funds")
#     return balance - amount    
# withdraw(1000,300)
f = open("test_file.txt", "w", encoding="utf-8")
f.write("مرحبا، ده أول ملف بعمله ببايثون")
f.close()