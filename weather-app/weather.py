from tkinter import *

from tkinter import messagebox
from time import strptime
from datetime import datetime

import requests
from PIL import ImageTk, Image


window = Tk()
window.geometry('800x400')
window.title('Weather')
window.resizable(0, 0)

def weather_data(query):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&appid=06c921750b9a82d8f5d1294e1586276f')
    return res.json()


#Body UI
Frame(window, width=800, height=50, bg='#353535').place(x=0, y=0)

# Search Bar
img1 = ImageTk.PhotoImage(Image.open('search.png'))
def on_enter(e):
    e1.delete(0, 'end')

def on_leave(e):
    if e1.get() == '':
        e1.insert(0, 'Search City')

e1 = Entry(window, width=21, fg='white', bg="#353535", border=0)
e1.config(font=('Calibri (Body)', 12))
e1.bind("<FocusIn>", on_enter)
e1.bind("<FocusOut>", on_leave)
e1.insert(0, 'Search City')
e1.place(x=620, y=15)

#date

#day
a = datetime.today().strftime('%B')
b=(a.upper())

#month
q= datetime.now().month

#time
now = datetime.now()

c = now.strftime('%B')
month = c[0:3]

today = datetime.today()
date = today.strftime("%d")



window.mainloop()

