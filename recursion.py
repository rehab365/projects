# Iterative
def walk(steps):
     for step in range(1, steps + 1):
        print(f"you take step # {step}")


walk(100)        
#recursive
def walk(steps):
     if steps == 0:
         return
     walk(steps-1)
     print(f"you take step # {steps}")
walk(100)    
#Mutual Recursion
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(4))  # True


#A Simple Example: Factorial
def factorial(n):
    if n == 0:                  # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))  # 120
#nasted
def sum_nested(data):
  total = 0
  for value in data.values():
    if isinstance(value, dict):
      total += sum_nested(value) # recurse
    else:
      total += value
  return total
print(sum_nested({"a": 1, "b": {"c": 2, "d": {"e": 3}}}))
