import requests
def stations():
  print('''LIST OF STATIONS
  1.LONDON       11.DUSSELDIRF    21.BREMEN
  2.MOSCOW       12.DRESDEN       22.ESSEN
  3.LJUBLJANA    13.HANOVER       23.DUISBERG
  4.BERLIN       14.LEIPZIG
  5.ROME         15.NUREMBERG
  6.MUNICH       16.FREIBURG
  7.HAMBURG      17.DORTMUND
  8.FRANKFURT    18.KARLSRUHE
  9.STUTTGART    19.MANNHEIM
  10.COLOGNE     20.HEIDELBERG''')
try:
  url = "https://flixbus2.p.rapidapi.com/trips"
  stations()
  departure_station = input("Enter the departure station: ").lower()
  arrival_station = input("Enter the arrival station: ").lower()
  date = input("Enter the date in the following format DD.MM.YYYY: ")
  adult = input("Enter number of adults 0 if none: ")
  children = input("Enter number of children 0 if none: ")
  #list of all bus stations and their ids
  bus_list = {
  "london" : "40dfdfd8-8646-11e6-9066-549f350fcb0c",
  "moscow" : "29e8a6b2-9ad1-484e-ae8c-aee9fd831ca6",
  "ljubljana" : "40de8044-8646-11e6-9066-549f350fcb0c",
  "berlin" : "40d8f682-8646-11e6-9066-549f350fcb0c",
  "rome" : "40de90ff-8646-11e6-9066-549f350fcb0c",
  "munich" : "40d901a5-8646-11e6-9066-549f350fcb0c",
  "hamburg" : "40d91e53-8646-11e6-9066-549f350fcb0c",
  "frankfurt" : "40d92162-8646-11e6-9066-549f350fcb0c",
  "stuttgart" : "40d90995-8646-11e6-9066-549f350fcb0c",
  "cologne" : "40d91025-8646-11e6-9066-549f350fcb0c",
  "dusseldorf" : "40d911c7-8646-11e6-9066-549f350fcb0c",
  "dresden" : "40db219f-8646-11e6-9066-549f350fcb0c",
  "hanover" : "40da4ac8-8646-11e6-9066-549f350fcb0c",
  "leipzig" : "40d917f9-8646-11e6-9066-549f350fcb0c",
  "nuremberg" : "40d90d0f-8646-11e6-9066-549f350fcb0c",
  "freiburg" : "40d8ff3b-8646-11e6-9066-549f350fcb0c",
  "dortmund" : "40da382b-8646-11e6-9066-549f350fcb0c",
  "karlsruhe" : "40d912c2-8646-11e6-9066-549f350fcb0c",
  "mannheim" : "40d90c3a-8646-11e6-9066-549f350fcb0c",
  "heidelberg" : "40d9068f-8646-11e6-9066-549f350fcb0c",
  "bremen" : "40da6e70-8646-11e6-9066-549f350fcb0c",
  "essen" : "40da3d5e-8646-11e6-9066-549f350fcb0c",
  "duisburg" : "40da79b3-8646-11e6-9066-549f350fcb0c"
}
  querystring = {
  "from_id" : bus_list[departure_station],  
  "to_id" : bus_list[arrival_station],
  "date":date,
  "adult":adult,
  "children":children,
  "bikes":'0',
  "currency":"EUR"}

  headers = {
  "X-RapidAPI-Key": "1973bac5f8mshf0fd04b7d7d49fbp1dce50jsn56a46a23a197",
  "X-RapidAPI-Host": "flixbus2.p.rapidapi.com"
}

  response = requests.get(url, headers=headers,   params=querystring)

  output = response.json()
  bus_info = output['journeys']
  print("\n")
  if 'error' not in bus_info[0]:
    print(f"TOTAL {len(bus_info)} BUSES ARE AVAILABLE\n")
    for i in range(len(bus_info)):
      print(f"The {i+1}th bus details: \n")
  
      print('The bus departs from the bus station:')
      print(bus_info[i]['dep_name'])
      print()
  
      print('The bus arrives to the bus station:')
      print(bus_info[i]['arr_name'])
      print()
  
      date,time = bus_info[i]['dep_offset'].split('T')
      time = time.split('.')
      time = time[0][:5]
      print(f'''The bus departs at:
      date: {date}
      Time: {time}''')
      print()
  
      date,time = bus_info[i]['arr_offset'].split('T')
      time = time.split('.')
      time = time[0][:5]
      print(f'''The bus arrives at:
      date: {date}
      time: {time}''')
      print()
  
      h,m = bus_info[i]['duration'].split(':')
      print(f"The bus travels for {h} hours {m} minutes")
      print()
      fare = bus_info[i]['fares'][0]
      print(f"Total fare is: {fare['price']}€")
      if 'additional_info' not in fare:
        print("The seats are not available")
      else:
        print(fare['additional_info'])
      print("\n")
  else:
      print(bus_info[0]['message'])
except:
  print("Enter valid details")