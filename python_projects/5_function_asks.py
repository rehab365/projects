#first task
def greeting(name):
    print(f"How are you {name}")
greeting("Rehab")
greeting("Hisham")
greeting("lovers")    
#second task
def calculate_discount(the_real_price=1000,discount=0.20):
    return the_real_price-(the_real_price * discount)

print(calculate_discount())
print(calculate_discount(2000,0.30))

#return vs print
def greet(name):
    print("Hello",name)
result=greet("Ahmed")    
print(result)  # NOne
#Multiple Parameters
def describe_sudent(name,age,city):
    return f"{name},age {age},from {city}"
print(describe_sudent("Ahmed", 26 , "Cairo"))
#Default Parameter Values
def descount_price(real_price=100,discount=0.3):
    return real_price-(real_price*discount) 
print(descount_price(1000,0.3))
#Returning Multiple Values
def get_min_max(number):
    return min(number),max(number)
lowest_highest=get_min_max([300,500,1000000,990,20])
print(lowest_highest)
#Returning Multiple Values
X = 10# global variables def cannot read it
def show_x():
   X=5
print(X) #10 
#The Mutable Default Argument Trap
def unique_letters(word):
    return set(word)
set=unique_letters("I love python")
print(set)
def add_item(item,cart=[]): # lists mutable one
    cart.append(item)
    return cart
print(add_item("apple"))
print(add_item("banana")) # it starts with he first add no fresh
#fixed to avoid that mistake use None
def add_item(item,cart=None):
    if cart is None:
        cart=[]
        cart.append(item) 
        return cart
print(add_item("apple"))
print(add_item("banana"))
print(add_item("shampoo"))
#Docstrings —Writing Professional Functions
def calculate_price(price, discount=0.1):
    """
      Calculate a discounted price.
 price: the original price
     discount: fraction to subtract (default 10%)
      Returns: the final price after discount
   """
    return price - (price * discount)
print(calculate_price.__doc__)
help(calculate_price)
#Functions Calling Other Function
def is_valid_email(email):
    return "@"in email and email.endswith(".com")
def regaister_user(name,email):
      if not is_valid_email(email):
        return "Invalid email"
      return f"Registered{name}"
print(regaister_user("Ahmed","hhloio"))
# Capstone: Sorting a Dictionary by Value
scores = {"Ahmed": 88, "Sara": 92, "Bilal": 79}
def get_score(pair):
  return pair[1] # واحد ياعني الاسكور عشان صفر الاسم 
#scores.items() produces: [("Ahmed", 88), ("Sara", 92), ("Bilal", 79)].                                    
#key=get_score tells Python: “Sort these tuples based on the score (second element).”
#reverse=True means sort in descending order (highest score first).
ranked = sorted(scores.items(), key=get_score, reverse=True)
print(ranked)