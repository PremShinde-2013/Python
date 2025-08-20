# import math

# class Shape:
#     def area(self):
#         raise NotImplementedError("Define area in subclass.")

#     def describe(self):
#         return f"I am a {self.__class__.__name__}."

# class Rectangle(Shape):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#     def area(self):                         # override
#         return self.w * self.h

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):                         # override
#         return math.pi * (self.r ** 2)

# shapes = [Rectangle(3, 4), Circle(5)]


# class Triangle:
#     def __init__(self, b, h):
#         self.b, self.h = b, h
#     def area(self):
#         return 0.5 * self.b * self.h

# def total_area(figures):
#     # Works for any object that has .area() — no inheritance required
#     return sum(fig.area() for fig in figures)

# # Polymorphism: both have .area(), we don’t care *which* shape it is
# for s in shapes:
#     print(s.describe(), "Area:", round(s.area(), 2))
# print(total_area([Rectangle(3,4), Circle(5)]))


#    ************************************************************  Inheritance  ***********************************

class Cars:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
    
    def full_name(self):
        return f"{self.brand}, {self.model} "

class ElectricCar(Cars):
     def __init__(self, brand,model,battery_Size):
        super().__init__(brand,model)
        self.battery_Size = battery_Size

    
myEle = ElectricCar("Mahindra","be69",150)
# print(myEle.model)
# print(myEle.full_name())


mycar = Cars("Mahindra","be69")
# print(mycar.brand,mycar.model)
# print(mycar.full_name())
# print(isinstance(myEle ,Cars))

# print(isinstance(mycar,ElectricCar))

class Battery:
    def info(self):
        return "this is battery"

class Engine:
    def E_info(self):
        return "this is Engine"

class ElectricCarTwo(Battery,Engine,Cars):
    pass


my_new = ElectricCarTwo("tesla","model S")
print(my_new.info())
print(my_new.full_name())
print(my_new.E_info())