"""
Created on Tue Jul  4 11:44:28 2023

@author: eliane.schmid
"""

import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_map")

map_test = folium.Map(location=(53.5450, 9.9968), tiles="Stamen Toner", zoom_start=12)

park_data = {
    "Lohsepark": 2016,
    "Sandtorpark": 2011,
    "Grasbrookpark": 2013,
    "Park Fiction": 1995,
    "Baaken Park": 2019,
    "Ballinpark": 2007,
    "Stadtpark":1914,
    "Emil-Wendt-Park":1956,
    "Lohmühlenpark": 2004,
    "Alsterpark": 1953,
    "Planten un Blomen": 1821,
    "Alter Elbpark": 1837,
    "Elbpark Entenwerder": 1997,
    "Hammerpark":  1906,
    "Jenischpark":1835,
    "Altonaer Balkon":1638,
    "Loki-Schmidt-Garten":1986,
    "Hirschpark":1907,
    "Wilhelmsburger Inselpark":2013,
    "Eichbaumsee":1976,
    "Volkspark Altona":1914,
    "Wohlers Park":1979,
    "Sternschanzenpark":1866,
    "Hayns Park":1923,
    "Rüschpark":2006,
    "Gorch-Fock-Park ":"1920ies",
    "Schröders Elbpark": 1953,
    "Westerpark": 1785,  
    "Wesselhöftpark": 1953,
    "Luuspark": 1986,
    "Sven Simon Park": "1980ies", 
    "Römischer Garten": 1951,
    "Blankeneser Schinckels Park": 1902,
    "Waldpark Marienhöhe": "1970ies",
    "Blankenese Hessepark": 1926,
    "Goßlers Park": 1924,
    "Rathenaupark": 1922,
    "Grothpark": 1968,
    "Donners Park": 1911, #kolo
    "Heinepark": 1984,
    "Platz der Republik": 1895,
    "Kapitän Schröder Park": 2019,
    "Gustav-Mahler-Park": 2014,
    "Rotherbaum Große Moorweide": 1881,
    "Schwanenwik": 1953,#IGA 1953
    "Harvestehude Eichenpark ": 1530,
    "Lohmühlengrünzug": 2001,
    "Reiherstiegknie": 2013,
    "Trauns Park": 1925,
    "Spielplatz Sanitaspark": 1985

}

hamburg_latitude_range = (53.4, 53.7)
hamburg_longitude_range = (9.7, 10.3)



for park_name, year_built in park_data.items():
    location = park_name
    test_loc = geolocator.geocode(location)
    
    if test_loc is not None:
        latitude = round(test_loc.latitude, 5)
        longitude = round(test_loc.longitude, 5)
    
        
        
        # Check if the geocoded location is within Hamburg boundaries
        if (
            hamburg_latitude_range[0] <= latitude <= hamburg_latitude_range[1] and
            hamburg_longitude_range[0] <= longitude <= hamburg_longitude_range[1]
        ):
        
        #https://htmlcolorcodes.com/
   
            try:
                    # Attempt to convert year_built to integer
                year = int(year_built)
                    
                if year > 1973:
                    color = 'lightgreen'  # Dark green
                else:
                    color = 'green'
            except ValueError:
                color = 'green'  # Fallback for non-integer inputs
            
            popup_content = f"<b>{park_name}</b><br>Year Opened to Public: {year_built}<br>Coordinates: {latitude}, {longitude}"
            
            #https://fontawesome.com/v4/icons/
            
            folium.Marker(
                location=[test_loc.latitude, test_loc.longitude],
                popup=popup_content,
                icon=folium.Icon(color=color, icon='tree-deciduous')
            ).add_to(map_test)

map_test.save("Hamburg_moreparks.html")

   
