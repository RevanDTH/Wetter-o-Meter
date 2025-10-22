import json
import tkinter as ttk
from weather_utilities import *


root = ttk.Tk()

place_var = ttk.StringVar()

def make_prediction():
    place=place_var.get()
    place_resp = json.loads(get_place(place))
    weather = get_weather(str(place_resp["lat"]),str(place_resp["lon"]))
    weather_score = analyse_weather(weather)
    print(weather_score)
    jacket_advice_tk.config(text=str(weather_score)) ##This is just for debug reasons, I will replace this
    place_var.set("")

title_tk = ttk.Label(text="Wetter-o-Meter")

place_entry_tk = ttk.Entry(root,textvariable=place_var)

jacket_advice_tk = ttk.Label(text="-")

submit_button_tk = ttk.Button(root, text="Wetter checken", command=make_prediction)

title_tk.grid(row=0,column=0)
place_entry_tk.grid(row=1,column=0)
jacket_advice_tk.grid(row=2,column=0)
submit_button_tk.grid(row=3,column=0)

root.mainloop()