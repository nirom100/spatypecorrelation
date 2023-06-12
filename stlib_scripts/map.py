import folium
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import cm


#create folium world map and show every type according to its location / cluster
world_map= folium.Map(tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(world_map)

df = pd.read_csv('mapinput.txt',sep=" ", header=None)
df.columns = ["type", "Longitude", "Latitude", "Country", "Cluster"]

#create cmap array : amount of clusters
x = df["Cluster"].nunique()
colors_array = cm.hsv(np.linspace(0, 1, x+2))
rainbow = [mpl.colors.rgb2hex(rgb[:4]) for rgb in colors_array]




#for each type entry, create circlemarker according to cluster
for i in range(len(df)):
        cluster = df.iloc[i]['Cluster']
        lat = df.iloc[i]['Latitude']
        long = df.iloc[i]['Longitude']
        radius=5
        popup_text = """type : {}<br>
                        cluster : {}<br>"""
        popup_text = popup_text.format(df.iloc[i]['type'], df.iloc[i]['Cluster'])
        folium.CircleMarker(location = [lat, long],
                            radius=radius,
                            tooltip = popup_text,
                            color = rainbow[cluster],
                            fill =True,
                            fill_color = rainbow[cluster]).add_to(marker_cluster)

#show the map
world_map.save("map.html")
