# 1.  ClassWrite a class named , which should have the following data attributes:
#    (for the name of a pet)
#    (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
#    (for the pet’s age)
                
#   The  class should have an  method that creates these attributes. It should also have the following methods:

# Once you have written the class, write a program that creates an object of the class and prompts the user to enter the name, type, and age of his or her pet. This data should be stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.


class Pet:

    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def get_animal_type(self):
        return self.__animal_type
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

my_pet = Pet(
    input("What is the pet's name? "),
    input("What type of animal is the pet? "),
    int(input("What is the animal's age? "))
)

print(my_pet.get_name())
print(my_pet.get_animal_type())
print(my_pet.get_age())

    





