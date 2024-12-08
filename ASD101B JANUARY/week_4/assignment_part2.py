# Write a class definition named Car. The Car class should have data attributes for a car’s model, year, speed, and color. 

#  The class should also have the following:

# An _ _init_ _ method for the class. The method should accept an argument for each of the data attributes.

# Accessor and mutator methods for each data attribute.

# Create my_car is the name of a variable that references an object.

# Write a statement that use#s the my_car variable to call the accessor and mutator methods. 

# class Car
# attributes:
# - model
# - year
# - speed
# - color
# methods
# - get/set model
# - get/set year
# - get/set speed
# - get/set color
# __init__
# __str__

class Car:

    def __init__(self, model: str, year: int, speed: float, color: str):
        self.model = model
        self.year = year
        self.speed = speed
        self.color = color

    @property
    def model(self):
       return self.__model
    @model.setter
    def model(self, value):
     self.__model = value
    
    @property 
    def year(self):
       return self.__year
    @year.setter
    def year(self, value):
     self.__year = value

    @property
    def speed(self):
       return self.__speed
    @speed.setter
    def speed(self, value):
     self.__speed = value

    @property
    def color(self):
       return self.__color
    @color.setter
    def color (self, value):
       self.__color = value

    def __str__(self):
        return f"Car:{{model:{self.model}, year: {self.year}, speed: {self.speed}, color: {self.color}}}"
    
my_car = Car ("Honda Civic", 2009, 240,"Gray")
print(my_car)

my_car.color = "Skeletor Gray"
print(my_car)
