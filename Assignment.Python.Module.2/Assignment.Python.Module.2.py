#1
length = float(input ("Enter the length of a zander（in cm）: "))
if length < 42:
    print("The zander does not fulfill the size limit(42cm),the fish will be released back into the lake.")

#2
shipclass = input("Enter your class: ").upper()
if shipclass == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif shipclass == "A":
    print("A: above the car deck, equipped with a window.")
elif shipclass == "B":
    print("windowless cabin above the car deck.")
elif shipclass == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("The information entered is incorrect.")

#3
gender = input("Enter your gender(M/F): ").upper()
hemoglobin_value = float(input("Enter your hemoglobin value(in g/l): "))
if gender == "M":
    if hemoglobin_value < 117:
        print("your hemoglobin value is low")
    elif 155 < hemoglobin_value:
        print("your hemoglobin value is high")
    else:
        print("your hemoglobin value is normal")
if gender == "F":
    if hemoglobin_value < 134:
        print("your hemoglobin value is low")
    elif 167 < hemoglobin_value:
        print("your hemoglobin value is high")
    else:
        print("your hemoglobin value is normal")

#4
year=int(input("Enter your year: "))
if year % 100 == 0:
    if year % 400 == 0:
        print("This year is leap year")
    else:
        print("This year is not leap year")
if year % 100 != 0:
    if year % 4 == 0:
        print("This year is leap year")
    else:
        print("This year is not leap year")