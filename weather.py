import requests

API_KEY = "9619b36727d8701b83f92f28a8799bcf"
CITY = "Lagos"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"Weather in {CITY}: {description}, {temperature}°C")
else:
    print("Error:", response.status_code, response.text)
