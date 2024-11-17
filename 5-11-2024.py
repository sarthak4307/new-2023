# class Myfirstprogram:
#     print("Welcome to object or Object Oriented Programming")
# C=Myfirstprogram()
# print(C)




# class Rectangle:
#     length=0
#     width=0
# R1=Rectangle()
# print(Rectangle.length)
# print(R1.width)                     # passing attributes if the class




# class Rectangle:
#     l=int(input("Enter length: "))
#     w=int(input("Enter width: "))
# R2=Rectangle()
# print(R2.l*R2.w)




# class Methoddemo:
#     def Display_message(self):
#         print("Welcome to methods in a class")
# ob1=Methoddemo()          #object of the class
# ob1.Display_message()     #calling the method




# class Circle:
#     def Circle_area(self,radius):
#         return 3.14*radius**2
# ob2=Circle()
# print(ob2.Circle_area(5))



# # self parameter with instance variable
# class Practice:
#     x=5
#     def show(self,x):
#         print(x)
#         x=30
#         print(x)
#         print(x)
# ob = Practice()
# ob.show(50)




# class Self_demo:
#     def method_a(self):
#         print('now in method a')
#         print('i am method a')
#     def method_b(self):
#         print('in method b calling method a')
# a=Self_demo()
# a.method_b()




# class Prime_Checker:
#     def __init__(self, number):
#         self.number = number

#     def is_prime(self):
#         if self.number <= 1:
#             return False
#         for i in range(2, int(self.number ** 0.5) + 1):
#             if self.number % i == 0:
#                 return False
#         return True

# number = int(input("Enter a number: "))
# checker = PrimeChecker(number)
# if checker.is_prime():
#     print(number," is a prime number.")
# else:
#     print(number," is not a prime number.")




# class Armstrong_Checker:
#     def __init__(self,number):
#         self.number=number
#     def no_of_digits(self,n):
#         self.n=len(str(self.number))
#     def is_arm(self):
#         if 




# class Arm_check:
#     def __init__(self, number):
#         self.number = number

#     def is_armstrong(self):
#         digits = [int(d) for d in str(self.number)]
#         num_digits = len(digits)

#         sum_of_powers = sum(d ** num_digits for d in digits)

#         return sum_of_powers == self.number

# number = int(input("Enter number: "))
# checker = Arm_check(number)

# if checker.is_armstrong():
#     print(f"{number} is Armstrong")
# else:
#     print(f"{number} isn't Armstrong")



# WAP to find the number is pa;indrome or not
class PalindromeChecker:
    def __init__(self, number):
        self.number = number

    def is_palindrome(self):
        str_number = str(self.number)
        return str_number == str_number[::-1]

number = int(input("Enter a number: "))
checker = PalindromeChecker(number)

if checker.is_palindrome():
    print(number," is palindrome.")
else:
    print(number," isn't palindrome.")