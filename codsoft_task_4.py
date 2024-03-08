import tkinter as tk
import requests
from tkinter import messagebox

def weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        message = f'Temperature: {temperature}°C\nWeather: {weather_desc.capitalize()}'
        messagebox.showinfo('Weather Forecast', message)
    else:
        messagebox.showerror('Error', 'City not found. Please check the spelling.')

def get_weather():
    city = entry.get()
    api_key = "49f4c9e7e6f88bcd24a0286fdc250b72"
    weather(city, api_key)

# Create the main window
root = tk.Tk()
root.title('Weather Forecast')
root.geometry('400x200')

# Create and pack widgets
label = tk.Label(root, text='Enter city:', font=('Segoe UI', 15, 'bold'))
label.pack()
entry = tk.Entry(root)
entry.pack()

weather_button = tk.Button(root, text='Get Weather', command=get_weather, font=('Segoe UI', 10, 'bold'), bg="lightgreen")
weather_button.pack()

# Run the Tkinter event loop
root.mainloop()
