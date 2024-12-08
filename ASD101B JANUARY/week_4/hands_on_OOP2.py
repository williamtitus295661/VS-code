# 3. Personal  ClassDesign a class that holds the following personal data: 
# name, address, age, and phone number. Write appropriate accessor and mutator methods. Also, 
# write a program that creates three instances of the class. One instance should hold your information,
# and the other two should hold your friends’ or family members’ information.

class PersonalInformation:

    def __init__(self, name:str, address: str, age: int, phone_number: str):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value

    def __str__(self):
        return(
            f"  name: {self.name}\n"
            f"  address: {self.address}\n"
            f"  age: {self.phone_number}\n"
            "}"
        )

Bill = PersonalInformation ("William Titus", "429 Jackson st. ", 41,"724-544-6494")
Satan = PersonalInformation ("The Dark Lord","666 styx ave.", 36, "606-666-0636")
Ron = PersonalInformation ("Ronald Mcdonald", "123 eieio lane", 74, "123-098-4567")

print(Bill)
print(Satan)
print(Ron)


    
    
    
    
