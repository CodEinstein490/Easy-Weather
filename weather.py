def weather():
  place = input("PLACE: ")
  print(place)
  time.sleep(1)
  url = "https://wttr.in/{}".format(place)
  print("Displaying data...")
  final_weather = requests.get(url)
  print(final_weather.text)
