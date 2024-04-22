import pygal
from datetime import datetime
import pytz
from pygal.maps.world import COUNTRIES
from geopy.geocoders import Nominatim
from tkinter import *
import os
import requests
worldmap =  pygal.maps.world.World()
worldmap.title="Welcome to Time Zone Convertor"

def timezone_grabber(city):
    all_timezones=pytz.all_timezones
    indices = [i for i, s in enumerate(all_timezones) if city in s]
    idx = indices[0]
    timezone=datetime.now(pytz.timezone(all_timezones[idx]))
    return timezone

#read country from city name
def read_country(city):
    geolocator = Nominatim(user_agent="google") 
    location = geolocator.geocode(city, language="en")
    country= location.address.split(',')[-1]
    return country

#getting the code of the country based on the country name
def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

  
#plotting the country on world map on basis of code of each country
def plot_map(city):
    location_tz=timezone_grabber(city)
    date_location=location_tz.strftime('%d/%m/%Y\t%H:%M:%S')
    #time_location=location_tz.strftime('%H:%M:%S')
    country=read_country(city).strip()
    country_code=get_country_code(country)
    label=f'{city}\nDate and time-{date_location}'
    worldmap.add(label, {
        country_code : 1000,
    })
    worldmap.render_to_file('plot.svg')

root = Tk()

root.geometry( "200x200" )

label1 = Label( root , text = "Select the original city: " )
label1.pack()
options = [
    "Havana",
    "Madrid",
    "London",
    "Paris",
    "Kolkata",
    "Karachi",
    "Sydney",
    "Dubai",
    "Berlin",
    "Tokyo",
    "Lusaka",
]

clicked = StringVar()

clicked.set( "Kolkata" ) 
    
drop = OptionMenu( root , clicked , *options )
drop.pack()

label2 = Label( root , text = "Select the destination city: " )
label2.pack()
clicked2 = StringVar()

clicked2.set( "London" )
    
drop = OptionMenu( root , clicked2 , *options )
drop.pack()

def submission():
    plot_map(clicked.get())
    plot_map(clicked2.get())
    os.system('start plot.svg')

sbmtbutton = Button( root , text = "Submit" , command = submission, activebackground='Light Blue' ).pack()
root.mainloop()