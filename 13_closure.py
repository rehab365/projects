#def outer_function():
   # msg = "I am in a closure"
   # def inner_function():
    #    print(msg)
   # return inner_function()
#outer_function()
numbers  =[]  #----->global variable
def enter_numbers(x):
    numbers.append(x)
    print(numbers)
enter_numbers(5)
enter_numbers(10)
enter_numbers(15)
# closure a function in another function
def enter_numbers_outer():
    numbers =[]
    def enter_numbers_inner(x):
        numbers.append(x)
        print(numbers)
    return enter_numbers_inner
enter_numbers = enter_numbers_outer()
enter_numbers(5)
enter_numbers(10)
enter_numbers(15)
def Zaikr():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = Zaikr()
while True:
    Zaikr = input("Press + to count ")
    if Zaikr == "+":
        print(counter())
    elif Zaikr == "exit":
        break
    else:
        print("Wrong Input")    
