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

#8.1
import mysql.connector

def get_location_by_ICOA(ICAO):
    sql = f"SELECT id,ident, name, latitude_deg, longitude_deg FROM airport WHERE ident='{ICAO}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Hello! The airport {row[2]}（ICAO:{row[1]}） is located at latitude {row[3]} , longitude {row[4]}.")
    return

connection = mysql.connector.connect(
    host='127.0.0.1' ,
    port = '3306',
    database = 'flight_game',
    user = 'root',
    password = '12345',
    autocommit=True
         )
ICAO = input("Enter ICAO: ")
get_location_by_ICOA(ICAO)

#8.2
import mysql.connector
def get_information_by_area_code(area_code):
    sql = ("SELECT type,COUNT(airport.id) "
           "FROM airport " 
           "WHERE iso_country = %s "
           "GROUP BY type "
           "ORDER BY type ")
    cursor = connection.cursor()
    cursor.execute(sql, (area_code,))
    result = cursor.fetchall()
    if result:
        for row in result:
            print(f"Airport type: {row[0]}, Number of airports: {row[1]}")
    else:
        print("No airports found")
    return
connection = mysql.connector.connect(
    host='127.0.0.1' ,
    port = '3306',
    database = 'flight_game',
    user = 'root',
    password = '12345',
    autocommit=True
         )
area_code = input("Enter area code: ").upper()
get_information_by_area_code(area_code)

#8.3
import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host='127.0.0.1' ,
    port = '3306',
    database = 'flight_game',
    user = 'root',
    password = '12345',
    autocommit=True
         )

def get_distance_by_ICOA(ICAO):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql, (ICAO,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return (result['latitude_deg'], result['longitude_deg'])
    else:
        print(f'No data found for ICAO code {icoa_code}')
        return None

def calculate_distance(icao1, icao2):
    coords_1 = get_distance_by_ICOA(icao1)
    coords_2 = get_distance_by_ICOA(icao2)
    if coords_1 and coords_2:
        distance = geodesic(coords_1, coords_2).kilometers
        print(f'The distance between {icao1} and {icao2} is {distance:2f} kilometers')
    else:
        print(f'No data found for ICAO code {icoa_code}')

icao1 = input('Enter the ICAO code of the first airport: ')
icao2 = input('Enter the ICAO code of the second airport: ')
calculate_distance(icao1,icao2)
