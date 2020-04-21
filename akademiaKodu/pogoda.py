#  api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}

import requests

page = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl')
json = page.json()
temperature = json['main']['temp']
temp = round(temperature - 273.5, 2)
print(temp)
