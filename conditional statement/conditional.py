# age =int(input("Enter your age: "))

# if age >= 18:
#     print("you can fuck anyone you want")

# else:
#     print("you are too young to fuck anyone you want ")    

# user_name = input("enter your name : ")
# user_marks = int(input("enter your marks : "))

# if user_marks >= 90:
#     print(f"congratulations {user_name} you have got A grade")

# elif user_marks >= 80 and user_marks < 90:
#     print(f"congratulations {user_name} you have got B grade")

# elif user_marks >= 70 and user_marks < 80:
#     print(f"congratulations {user_name} you have got C grade")

# elif user_marks >= 60 and user_marks < 70:
#     print(f"congratulations {user_name} you have got D grade")

# else:
#     print(f"sorry {user_name} you have failed the exam")            

# num = int(input("Enter a number: "))

# if num > 0:
#     print(f"{num} is a positive number")

# elif num < 0:
#     print(f"{num} is a negative number")

# else:
#     print(f"{num} is zero")    

# Q1. Variable creation

# # Apna name, age aur city store karne ke liye 3 variables banao aur print karo
# name = "Rahul"
# age =22
# city ="Jaipur"

# print(f"my name us {name} and my age is {age} and i live in {city}")
# print(type(name))
# print(type(age))
# print(type(city))

# Q2. Data types

# Ek int, float, string aur boolean variable banao aur sabka type print karo.

# int_var = 10
# flot_var =11.5
# str_var = "RAHUL"

# print(type(int_var))
# print(type(flot_var))
# print(type(str_var))

# Q3. Type casting

# x = '250' ko integer mein convert karo aur usmein 50 add karke print karo.

# x = '250'
# y =  int(x) +50
# print(y, type(y))


# name = input("Enter your name: ")

# print("Uppercase:", name.upper())
# print("Lowercase:", name.lower())
# print("Length:", len(name))
# print("First character:", name[0])
# print("Last character:", name[-1])
# print("Reversed name:", name[::-1])


# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is an even number")

# else:
#     print(f"{num} is an odd number")        

# num1 = int(input("Enter a: "))
# num2 = int(input("Enter b: "))
# num3 = int(input("Enter c: "))

# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the largest number")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the largest number")
# else:
#     print(f"{num3} is the largest number")

from posixpath import sep


# month =int(input("enter the number" ))

# if month ==1:
#     print("january")

# elif month==2:
#     print("february")

# elif month==3:
#     print("march")
# elif month==4:
#     print("april")
# elif month==5:
#     print("may")
# elif month==6:
#     print("june")
# elif month==7:
#     print("july") 
# elif month==8:
#     print("august")
# elif month==9:
#     print("september")
# elif month==10:
#     print("october")
# elif month==11:
#     print("november")        
# elif month==12:
#     print("december")    

marks =int(input("enter the marks"))

if marks >=90 and marks <=100:
    print("grade a")

elif marks >=80 and marks <90:
    print("grade b")

elif marks >=70 and marks <80:
    print("grade c")
elif marks >=60 and marks <70:
    print("grade d")

else:
    print("fail")
         
