import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(infile)

json.dump(eq_data, outfile, indent=4)

list_of_eqs = eq_data["features"]

mags = []
longitude = []
latitude = []

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    longit = eq["geometry"]["coordinates"][0]
    latit = eq["geometry"]["coordinates"][1]
    mags.append(mag)
    longitude.append(longit)
    latitude.append(latit)

print(mags[:10])
print(longitude[:10])
print(latitude[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": longitude,
        "lat": latitude,
        "marker": {
            "size": [5 * mag for mag in mags],
            "color": mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_earthquakes.html")
