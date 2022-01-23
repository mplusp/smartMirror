import tkinter as tk
from tkinter import *
import api.open_weather as open_weather
from time import strftime

CELSIUS = "°C"
selectedCity = "Hanau"

# weather functions
def get_current_weather(city):
    return open_weather.city_current(city)


def get_forecast(city):
    return open_weather.city_forecast(city)


def currentTemperature(city):
    data = get_current_weather(city)
    temp = data["main"]["temp"]
    currentTemperatureLabel.config(
        text="Current weather in " + selectedCity + ": " + str(temp) + CELSIUS
    )
    currentTemperatureLabel.after(360000, currentTemperature, city)


# clock function
def time():
    string = strftime("%H:%M:%S")
    clockLabel.config(text=string)
    clockLabel.after(1000, time)


# create screen
screen = tk.Tk()
screen.title("Magic Mirror")
screen.configure(background="black")
screen.geometry("480x320")
# screen.attributes("-fullscreen", True)

# clock ui
clockLabel = Label(screen, font=("calibri", 40, "bold"), bg="black", fg="white")
clockLabel.grid(column=2)
time()

# weather ui
currentTemperatureLabel = Label(screen, font=("calibri", 20), bg="black", fg="white")
currentTemperatureLabel.grid(row=0, column=0, padx=10, pady=2, sticky=W)

forecastFrame = Frame(screen, bg="black")


def build_forecast(city):
    data = get_forecast(city)
    for i in range(7):
        day = data["daily"][i]
        dayTemp = day["temp"]["day"]
        dayWeather = day["weather"][0]["description"]
        labelText = (
            "Day " + str(i + 1) + ": " + str(dayTemp) + CELSIUS + ", " + str(dayWeather)
        )
        label = Label(forecastFrame, text=labelText, bg="black", fg="white")
        label.grid(row=i, column=0, padx=10, pady=2, sticky=W)


build_forecast(selectedCity)
forecastFrame.grid(row=1, column=0, pady=2, sticky=W)
forecastFrame.after(360000, build_forecast, selectedCity)
currentTemperature(selectedCity)

mainloop()
