# # class Employee:
# #     def __init__(self, name, salary):
# #         self.salary = salary
# #         self.name = name

# #     def mystr(self):
# #         for employee in employees:
# #             print(f"My name is {employee.name} and earn {employee.salary} salary")
# #         employee.mystr()
# # employees = [
# #     Employee("ali", 2000),
# #     Employee("alw", 2000),
# #     Employee("aliw", 2000)
# #      ]        

# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# #   def myfunc(self):
# #     print("Hello my name is " + self.name)

# # p1 = Person("John", 36)
# # p1.myfunc()


# # # class Animal:
# # #     def __init__(self, name, specie):
# # #       self.name = name
# # #       self.specie = specie
# # #     def printout(self):
# # #   []     print(f"my name is {self.name} and i belong to the {self.specie} specie")
# # # class Cat(Animal):
# # #    def __init__(self, name, specie, sound, walk):
# # #     Animal.__init__(self, name, specie):
# # # class Cat(Animal):
# # #    def __init__(self, name, specie, walk, sound):
# # #     Animal.__init__(self, name, specie)
# # #     self.sound = sound
# #     # self.walk = walk  ``

# # # class Student(Person):
# # #    def __init__(self, fname, lname):
# # #       super().__init__(fname, lname)

# # class Person:
# #   def __init__(self, fname, lname):
# #     self.firstname = fname
# #     self.lastname = lname

# #   def printname(self):
# #     print(self.firstname, self.lastname)

# # class Student(Person):
# #  def __init__(self, fname, lname):
# #     super().__init__(fname, lname)
    
# #     self.age = 25

# # x = Student("Mike", "Olsen")
# # print(x.age)

# # class Person:
# #   def __init__(self, fname, lname):
# #     self.firstname = fname
# #     self.lastname = lname

# #   def printname(self):
# #     print(self.firstname, self.lastname)

# # class Student(Person):
# #   def __init__(self, fname, lname):
# #     super().__init__(fname, lname)
# #     self.graduationyear = 2019

# # x = Student("Mike", "Olsen")
# # print(x.graduationyear)

# # class Animal:
# #     def __init__(self, name, breed):
# #         self.name = name
# #         self.breed = breed

# #     def speak(self):
# #        pass

# # class Dog(Animal):
# #     def __init__(self, name, breed):
# #       super().__init__(name, "Dog")
# #       self.breed = breed
    
# #     def speak(self):
# #        return f"{self.name} says Meow and its a {self.breed}"
    
# # dog = Dog("Bingo", "Local Dog")
# # print(dog.speak())


# #Assignment : 1.creat a function to find a acount by account number
# #2. create a function to find an employee by id

# class Account:
#     database = [] 
#     def __init__(self, id, name, acc_number, balance):
#         self.id = id
#         self.name = name
#         self.balance = balance
#         self.acc_number = acc_number

#     def create(self):
#         user_det = {
#             "id": self.id,
#             "name": self.name,
#             "acc_number": self.acc_number,
#             "balance": self.balance
#         }
#         Account.database.append(user_det)
#         print(f"Dear {self.name}, your account number is {self.acc_number}, Your account has been created successfully")

#     def deposit(self, amount):
#        self.balance += amount 
#        print(f"{amount} has been credited to your acc and your account balance is {self.balance}")
    
#     @property
#     def balance(self):
#         return self.__balance
    
#     @balance.setter
#     def balance(self, number):
#         self.__balance = number

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#            print("insufficient fund")
   

#     def transfer(self, to_acc, amount):
#     # for acc in Account.database:
#         to_account = self.find_acc(to_acc)
#         # if acc["acc_number"] == to_acc:
#         if to_account:
#             if self.balance >= amount:
#                     self.balance -= amount
#                     to_account["balance"] += amount
#                     print(f"{amount} has been transfered to {to_acc}")
#             else:
#                 print("insufficient fund")
         
#         else:
#              print("account does not exist")
    
                
#     def find_acc(self, acc_to_find):
#         for acc in Account.database:
#             if acc["acc_number"] == acc_to_find:
#                 print(f"user: {acc["name"]}, account number: {acc["balance"]}, account balance: {acc["balance"]}")  
#                 return acc
#             else:
#                 print(f"account number {acc_to_find} does not exist")  
#                 return None
#     def view_details(self):
#        print(f"Dear {self.name}, your account number is {self.acc_number} and you have ${self.balance}")


# # user1 = Account(1, "soji", 2345, 5000)
# # user2 = Account(2, "bilii", 2347, 5000)
# # user1.create()
# # user2.create()
# # # user1.deposit(1000)
# # # user1.withdraw(1500)
# # user1.transfer(34455, 5000)
# # user1.transfer(2345, 5000)

# # user1.view_details()
# # for account in Account.database:
# #     print(f"user: {account["name"]}, account number: {account["balance"]}, account balance: {account["balance"]}")


# # class Dog:
# #     __number = 0
# #     def __init__(self, name):
# #         self.name = name
# #         Dog.__number += 1
# #         self.dognumber = Dog.__number
        
# #     def bark(self):
# #           print(f"{self.name} says woof")


# # jack = Dog("Jack")
# # print(jack.dognumber)


# # class Ems:
    
# #     system = []
# #     def __init__(self, name, salary) :
# #         self.name = name
# #         self.salary = salary

# #     def create(self):
# #         Ems.system.append(self)
# #         print(f"Dear {self.name} with salary")
    
# #     def delete(self):
# #         print()


# class Employee:
#     employee_database = []
#     def __init__(self, id, name,role, salary):
#                 self.id = id 
#                 self.name = name
#                 self.role =role
#                 self.salary = salary

#     def create(self):
#         employee = {
#             "id": self.id,
#             "name": self.name,
#             "role": self.role,
#             "salary": self.salary
#         }
#         Employee.employee_database.append(employee)
#         print(f"Dear {self.name} your account has been created")

#     def delete(self, employee_id):
#         search = self.find_employee(employee_id)
#         if search:
#             del search 
#             print(f"{search["name"]} details has been deleted")
#             # return search

#     def find_employee(self, employee_id):
#         for employ in Employee.employee_database:
#             if employ["id"] == employee_id 
#                 print(f"name: {employ["name"]}, salary: {employ["salary"]}, role:{employ["role"]}") 
#                 return employ
#             else:
#                 return None

# employee1 = Employee(1, "kaffy", "manager", 5000)
# employee2 = Employee(2, "Simi", "intern", 5000)

# employee1.create()
# employee2.create()
# employee1.find_employee(2)
# employee1.delete(1)
# print(employee1.id)
# for employee in Employee.employee_database:
#     print(f"user: {employee["name"]}, role: {employee["role"]}, salary: {employee["salary"]}")


tables = [{
'number': 1, 
    'seat': 2
},
{
'number': 2, 
    'seat': 4
},
{
'number': 3, 
    'seat': 4
},
{
'number': 4, 
    'seat': 8
}
    
]

class Reservation:
    Reserved_tables = []

    # reserved= [r for r in r['name'] in Reservation.Reserved_tables]

    def __init__(self, name, contact, party_size, date, time):
        self.name = name
        self.contact = contact
        self.party_size = party_size
        self.date = date
        self.time = time

    def make_reservation(self):
        available_tables = [table for table in tables if tables['seats'] >= self.party_size  and table['number'] not in [reserved_tables['table_number'] for reserved_tables in Reservation.Reserved_tables]] 
        user_details
        Reserve
        # print(available_tables)

    def cancel_resrvation(self):
        pass

user1 = Reservation("kafeelah", '080232695', 3,  2-3-1993, 6 )
user1.make_reservation()

# def menu():
#     while True:
#         print("1. make Reservation\n2. view eservation\n3. cancel reservation")
        
#         menu = input("Enter option number")
#         if menu == 1:

#             Reservation.make_reservation()
















