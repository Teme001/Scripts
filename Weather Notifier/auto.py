import requests
from plyer import notification
import datetime

API_KEY = "12345678"  # Replace with your API key
CITY = "Silver Springs"  # Replace with your city or prompt for input

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    
    if weather_data["cod"] != 200:
        print("Error fetching weather data:", weather_data["message"])
        return None
    
    temp = weather_data["main"]["temp"]
    condition = weather_data["weather"][0]["description"]
    return temp, condition

def send_notification(temp, condition):
    message = f"The temperature in {CITY} is {temp}°C with {condition}."
    notification.notify(
        title="Weather Update",
        message=message,
        timeout=10
    )

def main():
    temp, condition = get_weather()
    if temp is not None:
        send_notification(temp, condition)
        print("Notification sent!")
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    main()
