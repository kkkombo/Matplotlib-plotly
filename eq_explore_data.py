import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent = 4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for dict_ext in all_eq_dicts:
    mags.append(dict_ext['properties']['mag'])
    lons.append(dict_ext['geometry']['coordinates'][0])
    lats.append(dict_ext['geometry']['coordinates'][1])
    hover_texts.append(dict_ext['properties']['title'])

# Map the earthquakes.
# Map with list.
# data = [Scattergeo(lon = lons, lat = lats)]

# Map with dictionary.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}, 
    },
}]
my_layout = Layout(title = all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'global_earthquakes.html')