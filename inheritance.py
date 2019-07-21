"""
OOP inheritance and polymorphism to define Employee, Developer and Manager classes
"""

class Employee(object):
    """ Inheritance allows the child class to inherit the methods from the parent class.  """
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    """
    Polymorphism lets us define methods in the child class that have the same name as
    the attributes/ methods in the parent class. Inheritence lets this child class get all
    it's parents attributes and methods for free.
    """
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("--> ", emp.fullname())


# create objects
d1 = Developer("Corey", "Schafer", 50000, "Python")
d2 = Developer("Tom", "Smith", 60000, "Java")
m1 = Manager("Sue", "Smith", 90000, [d1])

# output developer name
print(f"My name is {d1.first} and I progam in {d1.prog_lang}")

# add / remove an employee to / from a manager
m1.print_emps()
m1.add_emp(d2)
print("Added employee")
m1.print_emps()
m1.remove_emp(d1)
print("Removed employee")
m1.print_emps()

# is manager a subclass of employee
print(issubclass(Manager, Employee)) # true