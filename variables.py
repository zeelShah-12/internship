#variables-basic
first_name = "jason"
last_name = "cabina"
full_name = "mahi ya"
country = "India"
city = "ahmedabad"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on= False
life,dream,food="song","die","allegry"
print(first_name,last_name,full_name,country,city,age,year,is_married,is_true,is_light_on,life,dream,food ,sep="\n")

#intermediate
# Check the data type of all your variables using type() built-in function
print([type(x) for x in [life,age,is_light_on]])

#Compare the length of your first name and your last name
print("long name" if len(first_name) > len(last_name) else"long last name" if  len(last_name)> len(first_name) else "both equal")

# Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4
print(num_one,num_two)

# dd num_one and num_two and assign the value to a variable total
print(total := num_one + num_two)

# Subtract num_two from num_one and assign the value to a variable diff
print(diff := num_two - num_one)

# Multiply num_two and num_one and assign the value to a variable product
print(product:= num_one * num_two)

# Divide num_one by num_two and assign the value to a variable division
print(division := num_one / num_two)

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
print(remainder := num_one % num_two)

# Calculate num_one to the power of num_two and assign the value to a variable exp
print(exp := num_one ** num_two)

# Find floor division of num_one by num_two and assign the value to a variable floor_division
print(floor_division := num_two // num_one)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_names = input("please enter your first name")
last_names = input("please enter your last name")
countrys = str(input("please enter your country"))
ages = int(input("please enter your age"))
print(f"hey its me {first_names} {last_names} from {countrys} i'm {ages} au revoir!")

# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
import math
user_radius = float(input("please enter your radius"))
area_of_circle = math.pi*(user_radius**2)
print(area_of_circle)