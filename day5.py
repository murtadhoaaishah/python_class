# Employees = [
#     {
#         "name": "Kilanko",
        
#             "details":{
#             "age":92,
#             "position": "cleaner",
#             "tasks": 
#             [
#                 "paint house",
#                 "fuel gen",
#                 "sweep the floor"
#             ]

#     }
        
#     },
#      {
#         "name": "Laide",
        
#             "details":{
#             "age":942,
#             "position": "cook",
#             "tasks": 
#             [
#                 "prepare dinner",
#                 "cut vegies",
#                 "make Eba"
#             ]

#     }
        
#     },
#      {
#         "name": "Khadeejah",
        
#             "details":{
#             "age": 58,
#             "position": "software developer",
#             "tasks": 
#             [
#                 "coding",
#                 "debugging",
#                 "designing"
#             ]

#     }
        
#     },
#      {
#         "name": "Yemi",
        
#             "details":{
#             "age":912,
#             "position": "trainer",
#             "tasks": 
#             [
#                 "train",
#             ]

#     }
        
#     },
#      {
#         "name": "Deborah",
        
#             "details":{
#             "age":92,
#             "position": "cleaner",
#             "tasks": 
#             [
#                 "cleaning"
#             ]

#     }
        
#     }
# ]
# employee1 = Employees[0]["details"]["tasks"][0]
# print(employee1)

# for employee in Employees:
#     print(employee["name"].upper())


# #iterator and generator
# list_instance = [1, 2, 3, 4, 5]
# iterator = iter(list_instance)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# def factors(n):
#     for val in range(1, n+1):
#         if n % val == 0:
#             yield val
# factors_of_20 = iter(factors(20))
# print(next(factors_of_20))
# print(next(factors_of_20))


# def employee():
#     for employee in Employees:
#         yield employee["name"].upper()
#         print(employee(employee["name"]))
# # employee_list = iter(employee())
# # print(next(employee_list))

# #Lamda function and mapping

# # employees =list(map(lamda x: x.upper(), employees)()

# num = [1, 2, 3,4]
# def square(num_list):
#     return [i**2 for i in num_list]
# print(square(num))
#lamda functions: inline functions, throw away functions
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
squares =[x**2 for x in num if x > 0 and x < 20 if x % 2 == 1]
print(squares)

prime =[n for n in num if all (n % i != 0 for i in range(2, n)) and n > 0]
print(prime)

word = ["shuh", "kabtdlen"]
capitalise = [n.capitalize() for n in word]
print(capitalise)

string = [n for n in word if len(n) >= 4]
print(string)
 
tuple = [(n, n**3) for n in num]
print(tuple)

# fizz = ["fizz" for i in range(0, 100) if i % 3 == 0  and  i > 0]
# print(fizz)
# Buzz = ["Buzz" for i in range(0, 100) if i % 5 == 0  and  i > 0]
# print(Buzz)
fizzbuzz = ["fizzBuzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i) for i in range(1, 101)]
print(fizzbuzz)

# def fizzbuzz(num: list):
#     for i in  range(0, 100):
#         if i % 15 == 0: 
#           print("fizzbuzz") 
#         elif:
#             if i % 5 == 0:
#                 print("buzz")
#         elif:
#             if i % 3 == 0:
#                 print("fizz")
#         else:
#            return i
# print(fizzbuzz(range(0, 100)))
