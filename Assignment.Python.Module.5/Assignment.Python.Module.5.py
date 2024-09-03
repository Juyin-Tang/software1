#1
import random
roll_number = int(input("Enter how many dice to roll: "))
roll = 0
number = []

while roll < roll_number:
    roll = roll + 1
    number.append(random.randint(1,6))
sum = sum(number)
print(f'the sum is {sum}')

#2
times = 0
list_number = []
number = input("Enter your number:" )
while number!= '':
    list_number.append(number)
    number = input("Enter your number:")
list_number.sort(reverse=True)
print(list_number[:5])

#3
number = int(input("Enter an integer:" ))
start_number = 2
if number <= 1 :
    print("The number is not a prime number.")
else:
    while start_number < number:
        if number % start_number == 0:
            print("The number is not a prime number.")
            break
        start_number += 1
    else:
        print("The number is prime number.")

#4
cities = []
city = input("Enter a city: ")
time = 1
while time <= 5 :
    cities.append(city)
    city = input("Enter a city: ")
    time += 1
for n in cities:
    print(n)
