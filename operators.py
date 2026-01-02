# #The Fitness Goal Tracker
# name=input("Enter your name: ")
# steps_today=int(input("How many steps today: "))
# steps_goal=int(input("How many steps goal: "))
# calories_burn=int(input("How many calories burn: "))
#
# total_calories=steps_today+calories_burn
# step_remaining=steps_goal-steps_today
# is_goal_achieve=steps_today>=steps_goal
# is_halfaway_done= steps_today >= (steps_goal / 2)
# is_super_star= is_goal_achieve and (total_calories >= steps_goal)
# boader="-"*30
#
# print(boader)
# print(f"fiteness report:{upper.name()}")
# print(f"steps_today:{steps_today}")
# print(f"step_remaining:{step_remaining}")
# print(f"total carolies:{total_calories:.2f}")
# print(f"is_goal_achieve:{is_goal_achieve}")
# print(f"is_halfaway_done:{is_halfaway_done}")
# print(f"is_super_star:{is_super_star}")
from variables import area_of_circle

# Arithmetic Operations in Python
# Integers

# print('addition:',12+2)
# print('subtraction:',12-2)
# print('multiplication:',12*2)
# print('division:',12/2)
# print('exponentiation:',12**2)
# print('remainder/modules:',12%2)
# print('remainder of division/Division without the remainder:',12//2)
#
# #Floats
# print("Floating Point Number, PI",3.14)
# print("Floating Point Number, gravity",9.54)
#
# #Complex numbers
# print("complex numbers:",1+1j)
# print('Multiplying complex numbers: ',(1 + 1j)*(1 - 1j))
#
# #declaring variable
#
# a=2
# b=12
#
# # Arithmetic operations and assigning the result to a variable
# print(f"addition:",a+b)
# print(f"subtraction:",a-b)
# print(f"multiplication:",a*b)
# print(f"division:",a/b)
# print(f"exponentiation:",a**b)
# print(f"remainder/modules:",a%b)
# print(f"remainder of division/Division without the remainder:",a//b)
#
# #small project: Calculating area of a circle
# radius=20
# area_of_circles=3.14* radius**2
# print(f"area of circle: {area_of_circles}")
#
# # area of rectangle
# length=2
# width=3
# area_of_rectangle =length * width
# print(f"area of rectangle: {area_of_rectangle}")
#
# #calculate the weight of object
# mass=76
# gravity= 9.2
# print(f"weight:{mass*gravity}")
#
# #calculate the density of liquid
# mass=77
# volume=7.1
# print(f"density:{mass/volume}")

#Comparison Operators

print(3>2)
print(4>=3)
print(3<=4)
print(4<3)
print(4==4)
print(3!=2)
print(len("mango")== len("apple"))
print(len("mango")!= len("apples"))
print(len("mango")< len("kiwi"))
print(len("mango")> len("cherry"))
print(len("dragon")== len("zebra"))
print('True == True :',True == True)
print('True == False :',True == False)
print('False == False :',False == False)

print('1 is 1:',1 is 1)
# print('1 is not  2:',1 is not 2)-------------------------
print('A in Ashi', 'A' in 'Ashi' )
print('z in xeel', 'Z' not in 'xeel')
# print('4 is 2**2',4 is 2**2)--------------------------

#Logical Operators
print(3<4 and 5>4)
print(5>4 or 4<5)
print(not 3<2)
print(not True)

#Example
# Declare age as integer variable
age:int = 25
print(age)

# Declare your height as a float variable
heigth:float = 3.14

# Declare a variable that store a complex number
me:complex = 2+ 12j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h)
base=int(input("please enter base"))
height=int(input("please enter height"))
area_of_traingle= area=0.5*base*height
print(area_of_traingle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a=int(input("please enter side a"))
side_b=int(input("please enter side b"))
side_c=int(input("please enter side c"))
print(perimeter_of_triangle:= side_a+side_b+side_c)
print(f"perimeter_of_triangle:",{perimeter_of_triangle})

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length= int(input("please enter length"))
width= int(input("please enter width"))
area_of_rectangle=2*(length*width)
print(f"area_of_rectangle:",{area_of_rectangle})

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius=int(input("please enter radius"))
area_of_circle=3.14*(radius**2)
circumference=2*3.14*radius
print(f"circumference:",{circumference})

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("dragon") == len("python"))

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("true" if "on" in "python" and "dragon" else "false")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("true" if "jargon" in "I hope this course is not full of jargon." else "false")

# Find the length of the text python and convert the value to float and convert it to string
result=float(len("python"))
print(result)
print(type(result))

# Check if int('9.8') is equal to 10
check = int(float('9.8')) == 10
print(check)

#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hour,rate=map(float,input("please enter your hours and rate per hrs:").split())
print(f"your weekly earning,{hour * rate:.2f}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years=int(input("please enter years you lived:"))
second_live=years*365*12*6*6

print(f"You have lived for {second_live} seconds")

# Write a Python script that displays the following table
for n in range(1,6):
    print(n,1,n,n**2,n**3)

#life analyzer

name=input("enter your name:")
age=int(input("age:"))
step_today=int(input("step today:"))
step_goal=int(input("step goal:"))
marks=float(input("marks:"))
attendance=float(input("attendance:"))
study_hours=float(input("study hours:"))

steps_remaining = step_goal-step_today
goal_achieve =step_today>= step_goal
half_done = step_today >=step_goal/2
pass_status =marks >=40 and attendance >=20

grade=(
    "A" if marks >=85 else "B" if marks >=70 else "C" if marks >=60 else "D" if marks >=50 else "Fail"
)
productivity= "High" if study_hours >=5 else "Low"

print(f"Name:,{name.upper()}")
print(f"Age:{age}")
print(f"Step today:{step_today}")
print(f"Step goal:{step_goal}")
print(f"Step remaining:{steps_remaining}")
print(f"Goal achieve:{goal_achieve}")
print(f"Halfway done:{half_done}")
print(f"Passing status :{pass_status}")
print(f"productivity:{productivity}")