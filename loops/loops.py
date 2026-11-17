# n = int(input("please tell me your number"))
                                    
# for i in range(n):
#     print("hello fucker")

# n = int(input("please tell me your number "))

# for i in range(1, n+1):
#     print(i)

# n =int(input("please tell me your number"))

# for i in range(n, 0, -1):
#     print(i)


# n = int(input("which number table you want "))

# for i in range (1, 11):
#     print(f"{n}* {i} ={n*i}")

# n = int(input("please tell me your number :- "))

# sum = 0

# for i in range(1, n+1):
#     sum = sum + i

# print(sum)

# n = int(input("please tell me your number :- "))

# fact = 1

# for i in range(1, n+1):
#     fact = fact  * i

# print(fact)


# n = int(input("tell me number :- "))

# even =0
# odd= 0
# for i in range(1,n+1):
#     if i%2  ==0:
#         even = even +i
#     else:
#         odd = odd +i

# print(f"your even and odd sum are {even},{odd} ")


# n = int(input("which number of factor you want :- "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)


# n = int(input("check is your number is perfect or not:- "))
# sum = 0
# for i in range(1, n):
#     if n%1 ==0:
#         sum = sum + i

# if sum ==n:
#     print("your number is perfect ")
# else:
#     print("your number is not perfect  ")


n = int(input("check is your number is prime or not:- "))

count = 0

for i in range(1,n+1):
    if n%i==0:
        count = count +1

if count ==2:
    print("your number is prime ") 
else:
    print("your number is not prime ")           