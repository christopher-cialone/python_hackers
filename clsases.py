# class MyClass:
#     a = 5
#     # print('Hola Mundo')

#     def hello(self):
#         print("Another Strange Message")

# myclass = MyClass()
# print(myclass.a)
# print(myclass.hello())


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} says woof!")

# # Creating an instance of Dog
# my_dog = Dog("Buddy", 3)

# # Accessing attributes and calling methods
# print(my_dog.name)  # Output: Buddy
# print(my_dog.age)   # Output: 3
# my_dog.bark()       # Output: Buddy says woof!
    
class RosaloneIndustries:
    def __init__(self, c_name, c_age, c_position):
        self.c_name = c_name
        self.c_age = c_age
        self.c_position = c_position

    def greet(self):
        print(f"{self.c_name} just joined the team")

rosalone_industries = RosaloneIndustries("Chris", 40, "Tech Lead")

print(rosalone_industries.c_name)
print(rosalone_industries.c_age)
print(rosalone_industries.c_position)
rosalone_industries.greet()
 
