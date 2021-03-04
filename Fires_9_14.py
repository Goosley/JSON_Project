import json

infile = open("US_fires_9_14.json", "r")
outfile = open("September_fire_data.json", "w")

September_data = json.load(infile)

json.dump(September_data, outfile, indent=4)

longs, lats, brightness = [], [], []

for i in September_data:
    lon = i["longitude"]
    lat = i["latitude"]
    bright = i["brightness"]
    longs.append(lon)
    lats.append(lat)
    if bright > 450:
        brightness.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": longs,
        "lat": lats,
        "marker": {
            "size": [0.02 * bright for bright in brightness],
            "color": brightness,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="Fires")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="September_Fires.html")
