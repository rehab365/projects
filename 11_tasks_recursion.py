# Write a recursive function that returns the sum of all numbers from 1 to n
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)
print(total(6))  # 15
# Write a recursive function that reverses a string (no slicing shortcuts)
def reverse_string(s):
     if len(s) == 0:   ## base case
         return s
     return s[-1] + reverse_string(s[:-1])# # recursive case
print(reverse_string("hello"))  # "olleh"
# Write a recursive function that counts how many times a value appears in a nested list
def sum_nasted(data):
    total=0
    for value in data:
        if  isinstance(value,list):
            total += sum_nasted(value) # recurse    
        else: 
            total += value
    return total   
print(sum_nasted([1, 2, [3, 4, [5, 6]], 7]))  # 28    
# lambda tasks
numbers = lambda n:n>10
print(numbers(15))
print(numbers(5.5))
length = lambda text: len(text)
print(length("python"))
print(length("hi there"))
#celsius = [0, 20, 30, 40]
#fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
#print(fahrenheit)


