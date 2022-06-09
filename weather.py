import requests

api_key = "67da29cb91129f1a68c1c06c1be92daa"
city = "Portland"
url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

request = requests.get(url)
json = request.json()

description = json.get("weather")[0].get("description")
print("Today's forcast is", description)

temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min, "degrees fahrenheit")
temp_max = json.get("main").get("temp_max")
print("The maximum temperature is", temp_max, "degrees fahrenheit" )