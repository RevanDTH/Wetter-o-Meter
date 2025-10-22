import tkinter as ttk
from weather_utilities import *


root = ttk.Tk()

place_var = ttk.StringVar()

def readPlace():
    place=place_var.get()
    print("Ausgewählter Ort: " + place)
    place_resp = get_place(place)
    weather = get_weather(getattr(place_resp, "lat"),getattr(place_resp, "lon")) ## FUNKTIONIERT NICHT, BITTE ÜBERARBEITEN
    place_var.set("")

title_tk = ttk.Label(text="Wetter-o-Meter")

place_entry_tk = ttk.Entry(root,textvariable=place_var)

submit_button_tk = ttk.Button(root, text="Wetter checken", command=readPlace)

title_tk.grid(row=0,column=0)
place_entry_tk.grid(row=1,column=0)
submit_button_tk.grid(row=2,column=0)

root.mainloop()