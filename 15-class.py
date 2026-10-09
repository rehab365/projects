# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#       return self.width * self.height   
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2

# c = Circle(5).area()
# print(c)

# r = Rectangle(4, 5)

# print(r.area()) 
# from abc import ABC,abstractmethod
# class Vehical(ABC):
#     @abstractmethod
#     def fuel_type(self):
#         pass
# class ElectricCar(Vehical):
#     def fuel_type(self):
#         print( "Electric")
# class PetrolCar(Vehical):
#     def fuel_type(self):
#         return "PetrolCar"      
# # v = Vehicle()      
# car1=ElectricCar()
# print(car1.fuel_type())      
# car2=PetrolCar()
# print(car2.fuel_type())       
    

      
class Dates:
    @staticmethod
    def to_dash_date(date):
        return date.replace("/", "-")
   
Date = Dates()
Date.to_dash_date("2023/06/15")
print(Date.to_dash_date("2023/06/15"))
        