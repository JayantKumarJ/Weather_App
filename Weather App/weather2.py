from tkinter import *
import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import sam1, sam2

#First Comment in git  

class WeatherApp:  
    def __init__(self, master):
        self.master=master
        style = tb.Style("vapor")
        master.title("Weather App")
        self.setup()
    
    def setup(self):

        lable1 = tb.Label(self.master, text="WEATHER APP", font=("helvetica", 28),bootstyle="light")
        lable1.pack(padx=10, pady=20)
    
        self.city_entry = tb.Entry(self.master, width=30)
        self.city_entry.pack(padx=10, pady=10)

        fetch_button = tb.Button(self.master, text="Get Weather", command=self.display)
        fetch_button.pack(padx=10, pady=10)

        self.temp_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.temp_label.pack(padx=10, pady=10)
        self.feels_like_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.feels_like_label.pack(padx=10, pady=10)
        self.min_tmp_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.min_tmp_label.pack(padx=10, pady=10)
        self.max_tmp_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.max_tmp_label.pack(padx=10, pady=10)
        self.pressure_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.pressure_label.pack(padx=10, pady=10)
        self.sea_level_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.sea_level_label.pack(padx=10, pady=10)
        self.humidity_label = tb.Label(self.master, text="",font=("helvetica", 10),bootstyle="light, inverse")
        self.humidity_label.pack(padx=10, pady=10)


    def display(self):
        input_data = self.city_entry.get()
        weather_data = sam2.WeatherInfo.get_weather(input_data)
        if weather_data:
            self.temp_label.config(text=f'Temperature: {weather_data["list"][0]["main"]["temp"]}')
            self.feels_like_label.config(text=f'Feels like: {weather_data["list"][0]["main"]["feels_like"]}')
            self.min_tmp_label.config(text=f'Minimum Temperature: {weather_data["list"][0]["main"]["temp_min"]}')
            self.max_tmp_label.config(text=f'Maximum Temperature: {weather_data["list"][0]["main"]["temp_max"]}')
            self.pressure_label.config(text=f'Atmospheric Pressure: {weather_data["list"][0]["main"]["pressure"]}')
            self.sea_level_label.config(text=f'Sea Level: {weather_data["list"][0]["main"]["sea_level"]}')
            self.humidity_label.config(text=f'Humidity: {weather_data["list"][0]["main"]["humidity"]}')

    
if __name__ == '__main__':
    root=tk.Tk()
    app=WeatherApp(root)
    root.geometry("360x640")
    root.mainloop()


