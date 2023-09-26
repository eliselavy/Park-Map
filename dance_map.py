import pandas as pd
import folium

location = "danse_sauvage_data.csv"
dance_station_locations = pd.read_csv(location)

dance_station_locations = dance_station_locations[
    ["main_place", "meeting_point", "latitude", "longitude", "date","url"]
]

# To create the map
# tiles="Stamen Toner"
# tiles="Stamen Terrain"
# tiles="Stamen Watercolor"
map = folium.Map(
    location=[
        dance_station_locations.latitude.mean(),
        dance_station_locations.longitude.mean(),
    ],
    tiles="Stamen Terrain",
    zoom_start=12,
    control_scale=True,
)

for index, location_info in dance_station_locations.iterrows():
 # Create a marker
    url = location_info['url']
    popup_content = f"<b>{location_info['main_place']}</b><br>Danse sauvage: {location_info['date']}<br>More info<a href='{url}' target='blank'> here</a>"
    color = "green"
    folium.Marker(
        [location_info["latitude"], location_info["longitude"]],
        icon=folium.Icon(color=color, icon='tree-deciduous'),
        popup=popup_content,
    ).add_to(map)
map.save("result/dance_sauvage.html")