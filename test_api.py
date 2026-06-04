import requests

API_KEY = "YOUR_API_KEY"

city = "Hyderabad"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

print("Program started")
print(response.json())