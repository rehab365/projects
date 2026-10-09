#keyword Arguments
def describe_student(name, age, city):
 return f"{name}, age {age}, from {city}"
print(describe_student("Ahmed", 25, "Karachi"))

#Returning Multiple Values
def get_min_max(numbers):
  return min(numbers), max(numbers)
lowest, highest = get_min_max([22, 8, 15, 16, 230])
print(lowest, highest) # 4 23
 #Scope: Local vs. Global Variables
x = 10 # global
def show_x():
 print(x)   # can read the global x just fine

def change_x():
 x = 5   # this creates a NEW local x — the global x is untouched
change_x()
print(x)
#The Mutable Default Argument Trap
def add_item(item,cart=[]):
   cart.append(item)
   return cart
print(add_item("apple"))
print(add_item("banana"))

def add_item(item,cart=None):
  if cart is None:
    cart=[]
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana"))
#Functions Calling Other Functions
def is_vaild_email(email):
  return "@" in email and email.endswith(".com")
def register_User(name,email):
   if not is_vaild_email(email):
    return"Invalid email"
   return f"Register {name}"
print(register_User("Ahmed", "ahmed@mail.com"))



