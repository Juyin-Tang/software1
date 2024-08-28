#1
numbers = 1
while numbers * 3 < 1000:
    mult_number = numbers * 3
    print(mult_number)
    numbers = numbers + 1

#2
inchers = int(input("Enter number of inches: "))
centimeters = inchers * 2.54
while inchers > 0:
    print(centimeters)
    inchers = int(input("Enter number of inches: "))

#3
numbers = float(input("Enter your number: "))
while numbers == " ":
    numbers = float(input("Enter your number: "))
    print(numbers)

#3
numbers = None
largest_number = numbers
smallest_number = numbers

while numbers != "":
    numbers = input("Enter your number: ")
    if numbers == "":
        print(smallest_number)
        print(largest_number)
        break
    elif  largest_number is None or int(largest_number) > int(numbers):
            largest_number = numbers
    elif smallest_number is None or smallest_number < numbers:
            smallest_number = numbers

#4
import random
number = int(random.randint(1, 10))
guess_number = 0
while guess_number != number:
    guess_number = int(input("Guess a number between 1 and 10: "))
    if guess_number > number:
        print("Too high!")
    elif guess_number < number:
        print("Too low!")
print("Correct!")

#5
right_name = "python"
right_password = "rules"
times = 1
name = input("What is your name? ")
password = input("What is your password? ")
while name != right_name and password != right_password:
    if times < 5:
        if name != right_name or password != right_password:
            print("Please try again.")
            times = times + 1
            name = input("What is your name? ")
            password = input("What is your password? ")
    else:
        print("Access denied.")
        break
if name == right_name and password == right_password:
    print("Welcome")

#6
import random
random_points = int(input("enter number of points: "))

inside_circle = 0
points = 0
while points < random_points:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
        inside_circle += 1
    points += 1
pai = 4 * inside_circle / random_points
print(f"the approximation of pi is {pai}")
