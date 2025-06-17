from importlib.resources import contents
from pathlib import Path
import json
import plotly.express as px
from turtle import title

#Read data as a string and convert to a Python object
#path = Path('Python/Chapter-16/weather_data/eq_data_1_day_m1.geojson')
path = Path('Python/Chapter-16/weather_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

#Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])
print(lons[:5])
print(lats[:5])
print(len(all_eq_dicts))

#Create a more readable version of the data file
path = Path('Python/Chapter-16/weather_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents, encoding="utf-8")

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags,
                     color_continuous_scale='Bluered',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     )
fig.show()