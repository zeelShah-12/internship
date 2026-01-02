# #Variables & Data Types
# #The Space Explorer Profile
# explorer_name=str(input("Enter your name: "))
# planets_visited=int(input("Enter your planets visited: "))
# fuel_remaining=float(input("Enter your fuel remaining: "))
# is_mission_active=bool(input("Enter your mission active: "))
# print("--mission brief--")
# print(f'planets_visited:{planets_visited}')
# print(f'fuel_remaining:{fuel_remaining}%')
# print(f'is_mission_active:{is_mission_active}')
# print(f'explorer_name:{explorer_name}')
# print(type(explorer_name))
# print(type(planets_visited))
# print(type(fuel_remaining))
# print(type(is_mission_active))
# ------------------basic-------------
# x=[1,2,3]
# y=x
# y.append(4)
# print(x)
import math

# x=2
# y=x
# y+=2
# print(x)
# print(y)

# x=10
# y=x
# x=20
# print(y)

# name="james"
# copy_name = name
# name="zeel"
# print(copy_name)

# nums=[1,2,3]
# ref=nums
# ref=[2,3,4]
# print(nums)
#
# a=5
# b=a
# b+=5
# print(a)
# print(b)

# x="100"
# y=int(x)
# y+=50
# print(x)
# print(y)

# x=300
# y=300
# print(x is y)
# print(x == y)

# a=[1,2,3]
# b=a
# b.append(4)
# print(a)

# x=[10,20]
# y=x
# y=[1,2]
# print(x )
# print(y)

# x=[1,2,3]
# y=(1,2,3)
# x.append(4)
# y[0]=4

# x=(2,3,4)
# print(x)
# x=(1,3,4)
# print(x)

# num=2
# if num % 2==0:
#     print("even")
# else:
#     print("odd")

# for i in range(1,11):
#     if  i %3==0:
#         print(i)

# count=5
# while count>0:
#     print(count)
#     count-=1

# count=1
# while count<= 10:
#     if count%2!=0:
#         print(count)
#     count+=1

# num=4
# if num == 0:
#     print("zero")
# elif num < 0:
#     print("negative")
# else:
#     print("positive")

# a,b=2,3
# a,b=b,a
# print(a,b)

# x=1
# x=x+1==2
# print(x)

# print(bool(0), bool(""), bool("0"))
# x = "2"
# print(x + x * 2)

# a = False
# b = True
# print(a == b, a is b)

# n=3
# if n%2!=0:
#     print("odd")
#     pass

# a = 1
# b = 1.0
# print(type(a + b))

# n="3.5"
# y=float(n)
# result=y+1.5
# print(result)

# list1=[1,2]
# list2= list1
# list2.append(3)
# print(list1)
# print(list2)

# n=3
# if n%2==0:
#     print("even")
# if n%3==0:
#     print(n)
# else:
#     pass

# n="45"
# y=int(n)
# result=y+10
# print(result)

# n=[1,2,3]
# n1 = n
# n1[1]=4
# print(n)
# print(n1)

# a,b=1,2
# a,b=b,a
# print(a)
# print(b)

# a="10"
# b=5
# c=2.5
# d=int(a)
# result=b+c
# print(result)
# print(type(d))
# print(type(result))

# x=7
# y=10
# result = x>5 and y<5
# print(result)

# a=[2,4,6,8]
# b=a
# b[0]=b[0]*2
# print(b)
# print(a)

# num_str=float("50")
# num_float= 25.5
# result= num_str - num_float
# print(result)

# n=12
# if n%3==0 and n%4==0:
#     print("fizzbuzz")
# elif n%3==0:
#     print("fizz")
# elif n%4==0:
#     print("buzz")
# else:
#     print(n)

# x=1000
# y=1000
# print( x==y and x is y)
#
# a=5
# b=3
# c=2
# result=(a+b)*c//b-a%c
# print(result)

# a="12"
# b=3
# # c=2.5
# print(int(a)+b+c)

# x=8
# y=15
# res= x>5 and y <20
# print(res)

# nums=[2,4,6]
# b=nums
# b[1]=b[1]*3
# print(b, nums)

# num_str = int("45")
# num_float=int(12.5)
# result=num_str-num_float
# print(result)

# n=20
# if n%3==0  and n%4==0:
#     print("fizzbuzz")
# elif n%3==0:
#     print("fizz")
# elif n%4==0:
#     print("buzz")
# else:
#     print(n)

# a=7
# b=5
# a,b=b,a
# print(a,b)

# a=5
# b=2
# c=3
# result=(a + b) * c // b - a % c
# print(result)

# x=7
# y=12
# res=x<10 and y%4==0
# print(res)

# n=[1,2,3]
# a=n[0]+5
# b=n[1]*2
# result=a+b
# print(type(result))

# a=int("15")
# b=4.5
# c=2
# result=(a + b) * c
# print(type(result))

# x=12
# y=25
# result =(10<= x<=20)  or (y%5==0)
# print(result)

# nums=[1,2,3,4]
# ref=nums
# ref[3]=ref[3]+5
# print(ref)

# num_str="100"
# num_int=45
# result=(int(num_str)-num_int)
# print(result)

# x=3
# y=4
# z=5
# result=(x + y * z) // (x + z)
# print(result)

# a=1
# b=0
# c=2
# result=a or b and c
# print(result)

# n=13
# print("positive" if n>0 else" negative" if n<0 else"zero")
# print("even" if n%2==0 else"odd")
#print("fizzbuzz"if n%3==0 and n%5==0 else "fizz" if n%3==0 else "buzz" if n%5==0 else "None")
#print("large" if n>50 else"small")

# Conditional Expressions (Ternary)
# print("low" if 1<=n <=10 else "Medium" if 11<=n <=50 else "high")
# print("prime" if n>1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1) )else "non prime" )
# # print("square" if (n**0.5).is_integer() else"not square")

#prime number logic
# n=5
# if n==2  or n==3:
#     print("prime")
# elif n<=1 or n%2==0:
#     print("non-prime")
# else:
#     print("prime")
# n= "1221"

# Digit Classification
# print("single digit" if 1<=n<=9 else "double digit" if 10<=n<=99 else"Multiple Digit")
# print(sum(int(digit) for digit in str(n)))

#Palindrome Checker
# print("palindrome" if n==n[::-1] else"not palindrome")

# Strong Number Checker
# n=123
# print("strong number" if sum(math.factorial(int(d)) for d in str(n))==n else "not strong number")

# Fuel Calculator
# dis=150
# mileage=12.5
# print(dis/mileage)

# Age in Days
# age=21
# print(age*365)

# Shopping Bill
# price=499.75
# quantity = 3
# total=price*quantity
# gst=total*0.18
# result=total+gst
# print(gst)
# print(total)
# print(result)

# Temperature Converter
# C=37
# F = (C * 9/5) + 32
# print(F)

# basic_salary=30000
# hra_percent = 20
# da_percent = 10
# HRA=hra_percent/100*basic_salary
# DA=da_percent/100*basic_salary
# total=basic_salary+HRA+DA
# print(total)

# time converter
# seconds=3671
# hours=math.floor(seconds/3600)
# minutes=math.floor(seconds/60)%60
# seconds=math.floor(seconds)
# print(hours,minutes,seconds)

# logical check
# marks= 82
# attendance=78
# print("True" if marks>=75 and attendance>=80 else "False")

# x=True
# y= False
# print(x+y)
# # print(x*10+y)

# amount=2400
# final=amount*0.90 if amount >=2000 else amount
# print(final)

# name=("zeel")
# print(len(name))

# name="zeel"
# last_name="shah"
# print("long name" if len(name) > len(last_name) else "Long last name" if len(name) < len(last_name) else "both equal")

