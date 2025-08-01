import requests

city = input("Enter City: ")
api_key = "YOUR_API_KEY"  

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
data = response.json()

print(data)  

if response.status_code == 200:
    print(f"Weather in {city}: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
else:
    print(f"Error: {data['message']}")
