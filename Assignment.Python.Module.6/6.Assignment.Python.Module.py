#1
import random
total_number = []

def toll():
    number = random.randint(1, 6)
    total_number.append(number)
    return
number = 0
while number != 6:
    number = random.randint(1, 6)
    toll()
print(total_number)

#2
maximum_number  = int(input("Enter a number: "))
import random
total_number = []
number = 0
def toll():
    number = random.randint(1, maximum_number)
    return number
while number != maximum_number:
    number = toll()
    total_number.append(number)
print(total_number)

#3
gallons = float(input("What is your gallons? "))
def converted():
    litres = gallons * 3,78541
while gallons >= 0:
    converted()
    print(f"The gallons is: {gallons}")
    gallons = float(input("What is your gallons? "))

#4
list = [1,2,3,4,5,6,7]
def addition(list):
    return sum(list)
total = addition(list)
print(total)

#5
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = []
def select(list_1):
    for i in list_1:
        if i % 2 == 0:
            list_2.append(i)
select(list_1)
print(list_2)

#6
import math
def calculate(diameter,price):
  radius_in_cm = diameter / 100 / 2
  area = math.pi * radius_in_cm ** 2
  return price / area

diameter_1 = float(input("The first pizza's diameter is (in centimeters): "))
price_1 = float(input("The first pizza's price is (in euros): "))
diameter_2 = float(input("The second pizza's diameter is (in centimeters): "))
price_2 = float(input("The second pizza's price is (in euros): "))

pizza_1 = calculate(diameter_1,price_1)
pizza_2 = calculate(diameter_2,price_2)

if pizza_1 > pizza_2:
  print("the second pizza is greater than the first pizza")
elif pizza_2 > pizza_1:
  print("the first pizza is greater than the second pizza")
else:
  print("tie")
