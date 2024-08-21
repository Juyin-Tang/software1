import math
#1
name = input("Enter your name: ")
print("Hello, " + name + "!")

#2
radius = float(input("Enter your radius: "))
area = math.pi*radius**2
print("the area is" + str(area))

#3
length = float(input("Enter your length: "))
width = float(input("Enter your width: "))
area = length * width
sum_of_the_lengths = (length + width) * 2
print(f"Your area of the rectangle is {area},\nYour perimeter of a rectangle is {sum_of_the_lengths}")

#4
first_mumber = float(input("Enter your frist number: "))
second_number = float(input("Enter your second number: "))
third_number = float(input("Enter your third number: "))
sum = first_mumber + second_number + third_number
product = first_mumber * second_number * third_number
avarage = sum / 3
print("The average is " + str(avarage))
print("The sum is " + str(sum))
print("The product is " + str(product))

#5
talents = float(input("Enter your number of talents: "))
pounds =  float(input("Enter your number of pounds: "))
lots = float(input("Enter your number of luoti: "))
pounds += talents * 20
lots += pounds * 32
grams = lots * 13.3
kilograms = grams/1000
print(f"{kilograms} kilograms and {grams} grams.")

#6
import random
dig_3 = str([random.randint(1,9) for i in range(3)])
dig_4 = str([random.randint(1,6) for i in range(4)])
print("3-digit code:" + dig_3)
print("4-digit code:" + dig_4)