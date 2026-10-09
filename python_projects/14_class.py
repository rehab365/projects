# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print(f"{self.name} says Woof!")   
# D1 = Dog("Bubby",5)
# D2 = Dog("Max",9)        #I have to write 2 prameters because the constructor has 2 parameters.
# D1.bark()
# D2.bark()
# print(D1.name)
# print(D2.name)
# class Car:
#    def __init__(self,brand,speed):
#          self.brand = brand
#          self.__speed = speed
#    def accelerate(self):
#         self.__speed= self.__speed+10
#         if self.__speed>10:
#          print(f"{self.brand} is accelerating to {self.__speed} km/h")   
          
#    def get_speed(self):
#     return self.__speed


# C1 =Car("Toyota",15)
# print(C1.get_speed)
# C1.accelerate() 
# C2 = Car("BMW",20)
# C2.accelerate()
# class Book:
#    def __init__(self,title,author,price):
#       self.title = title
#       self.author = author
#       self.__price = price
#    def get_price(self):
#       return self.__price
#    def set_price(self,new_price):
#       if new_price < 0:
#          print("Must be positive no")
#    def apply_discount(self, percentage):
#     discount_amount = self.__price * percentage / 100
#     self.__price = self.__price - discount_amount
# class EBook(Book):
#   no_of_E_book=0
#   def __init__(self,title,author,price,color):
#      super().__init__(title,author,price)
#      self.color = color
#      EBook.no_of_E_book += 1
# b1= Book("Python Basics","John",500)
# b2 = EBook("C++ Basics","Rehab",600,"Red")
# b2.apply_discount(20)
# print(b1.get_price())
# print(b2.get_price())
# print(b2.color)   

class BankAccount:
   bank_name="Bank Maser"
   def __init__(self,balance):
      self.__balance = balance      
   def deposit(self,amount):
      if amount>0:
         self.__balance+= amount
         print(f"Deposit made in {self.bank_name}،current balance is : {self.__balance}")
      else:
         print("must be positive")   
   def withdraw(self,amount):
     if amount > self.__balance:
       print("your amount is not enough")
     else:
        self.__balance -= amount
        print(f"Withdraw made in {self.bank_name}،current balance is : {self.__balance}") 
   def get_balance(self):
      return self.__balance      
   @property
   def balance(self):
     return self.__balance
   @balance.setter
   def balance(self,value):
    if value < 0:
      raise ValueError("رسالة مناسبة هنا ")
    else:
      self.__balance = value
acc1=BankAccount(10000)  
acc1.deposit(50)    
acc1.withdraw(1000)


      

   
      