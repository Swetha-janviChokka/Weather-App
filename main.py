from tkinter import *
import requests
from tkinter import messagebox
from datetime import datetime

API_KEY = "YOUR_API_KEY"

def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        if "cloud" in condition.lower():
            emoji = "☁"
        elif "rain" in condition.lower():
            emoji = "☂"
        elif "clear" in condition.lower():
            emoji = "☀"
        else:
            emoji = "⛅"

        temp_label.config(text=f"Temperature: {temp} °C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        condition_label.config(text=f"Condition: {emoji} {condition}")
    else:
        messagebox.showerror("Error", "City not found!")

        temp_label.config(text="Temperature:")
        humidity_label.config(text="Humidity:")
        condition_label.config(text="Condition:")
def update_time():
    current_time = datetime.now()
    time_label.config(text=current_time.strftime("%d-%m-%Y %H:%M:%S"))
    root.after(1000, update_time)
root = Tk()
root.title("Weather App")
root.geometry("500x500")
root.configure(bg="lightblue")

title = Label(
    root,
    text="🌦 Weather App",
    font=("Arial", 22, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

current_time = datetime.now()

time_label = Label(
    root,
    text=current_time.strftime("%d-%m-%Y %H:%M"),
    bg="lightblue"
)

time_label.pack()
update_time()
city_label = Label(root, text="Enter City Name", bg="lightblue")
city_label.pack()

city_entry = Entry(root, width=30)
city_entry.pack(pady=5)

search_button = Button(root, text="Search", command=get_weather)
search_button.pack(pady=10)

temp_label = Label(
    root,
    text="Temperature:",
    bg="lightblue",
    font=("Arial", 12))
temp_label.pack(pady=5)

humidity_label = Label(root, text="Humidity:", bg="lightblue")
humidity_label.pack(pady=5)

condition_label = Label(root, text="Condition:", bg="lightblue")
condition_label.pack(pady=5)
root.bind('<Return>', lambda event: get_weather())
root.mainloop()