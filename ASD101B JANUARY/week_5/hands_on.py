#  ClassWrite a class named  that holds the following data about an employee in attributes: 
# name, ID number, department, and job title.Once you have written the class, write a program that creates three  objects to hold the following data:
#   NameID NumberDepartmentJob TitleSusan Meyers47899AccountingVice PresidentMark Jones39119ITProgrammerJoy Rogers81774ManufacturingEngineer
# The program should store this data in the three objects, then display the data for each employee on the screen.

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def __str__(self):
        return "\n".join([
            "Employee {",
            f"  Name: {self.name}",
            f"  ID Number: {self.id_number}",
            f"  Department {self.department}",
            f"  Job Title: {self.job_title}",
            "}"
       ])
    
employees = [
    Employee("Susan Meyers" , 47999, "Accounting", "Vice Prresident"),
    Employee("Mark James" , 39119, "IT", "Programmer"),
    Employee("Joy Rogers", 81774, "Manufactoring", "Engineer"),
    ]
for employee in employees:
    print(employee)