#7.1
seasons = ("spring","summer","autumn","winter")
month_number = int(input("Enter the month number(1-12):"))
season = month_number/4
if season == 3 or season <= 0.5 :
    season_number  = 3
elif 0.5 < season <= 1.25 :
    season_number = 0
elif 1.25 < season <= 2 :
    season_number = 1
else:
    season_number = 2
month = seasons[season_number]
print(f"Month number {month_number} is {month}.")

#7.2
name = (input("What is your name? "))
time = 0
set_name = set()
while name != '':
  set_name.add(name)
  time += 1
  if time == 1:
    print("New name")
  name = (input("What is your name? "))
  if name in set_name:
    print("Existing name")
  else: print("New name")
print(set_name)

#7.3
airport_information = {}
print("Please choice your option.\n1.Enter a new airport\n2.Fetch the information of an existing airport\n3.Quit.")
choice = int(input("what would you like to do? "))
while choice != 3:

  if choice == 1:
    icao_code = input("Please enter the ICAO code: ")
    airport_name = input("Please enter the airport name: ")
    airport_information[icao_code] = airport_name

  elif choice == 2:
    code = input("Please enter the ICAO code: ")
    if code in airport_information:
      print(f" {code} is {airport_information[code]}")
  elif choice == 3:
    break
  choice = int(input("what would you like to do? "))
