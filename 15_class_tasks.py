class An_Embloyee:
    def __init__(self,name,salary):
       self.name=name
       self.__salary=salary
    def get_salary(self):
         return self.__salary   
    def raise_salary(self,perecentage):
      self.__salary = self.__salary + (self.__salary * perecentage/100) 
class Manager(An_Embloyee):
    def __init__(self,name,salary,team_size):
       super().__init__(name,salary) # super doesn't take self 
       self.team_size=team_size 
      
    def raise_salary(self, perecentage):
        return super().raise_salary(perecentage*2)   # super هي اللي بتتكفل self لوحدها
Em1=An_Embloyee("Ahmed",50000) 
Em1.raise_salary(10)
print(Em1.get_salary())
manager1=Manager("MR:Mohamed",20000,"50 members")
manager1.raise_salary(10)
print(manager1.get_salary())    
print(Em1.name) 
print(Em1.get_salary())
print(An_Embloyee.__mro__)


class Cat:
    def sound(self):print("كاكيككك")
class Dog:
    def sound(self):print("هوهوههووو")
class Cow:
    def sound(self):print("مأأأأأ")           
def call_sound(animal):
    animal.sound()
call_sound(Cat())
call_sound(Cow())
call_sound(Dog())   


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def __repr__(self):
        return f"student(name= {self.name!r} ,age= {self.age} )" 
student=Student("Rehab",22)    
print(student)
print(repr(student))            
    
