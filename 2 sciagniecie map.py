import urllib.request
from PIL import Image
import os
import math


import os
import urllib
import pandas as pd

import requests
import shutil


os.chdir('D:\KK\OneDrive\Wroclaw w Liczbach\Gotowe projekty\\20191219 zielone miasta')
print(os.getcwd())

#wczytanie API
with open(os.getcwd() + '\\apikey.txt') as f:
    apikey = f.readline()
    f.close 

################################################
x = 0    
######################################


#Wczytanie listy miast
addresses = pd.read_csv(os.getcwd() + "\\addresses_coord 2.csv")

#Ustalanie zmiennych
zoom=14
size_tile_x,size_tile_y=1024,1024
# Scale doubles the resolution
scale=2
format_image='png'
maptype='roadmap'
style=''
#style='&style=element:labels%7Cvisibility:off&style=feature:administrative.land_parcel%7Cvisibility:off&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:landscape.man_made%7Ccolor:0xff0000&style=feature:landscape.natural%7Ccolor:0xc42bd5&style=feature:landscape.natural.terrain%7Ccolor:0xc42bd5&style=feature:poi%7Celement:labels.text%7Cvisibility:off&style=feature:poi.business%7Cvisibility:off&style=feature:road%7Cvisibility:off&style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:transit%7Cvisibility:off'
style='&style=element:labels%7Cvisibility:off&style=feature:administrative%7Celement:geometry%7Cvisibility:off&style=feature:administrative.land_parcel%7Cvisibility:off&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:poi%7Cvisibility:off&style=feature:road%7Cvisibility:off&style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:transit%7Cvisibility:off'
#style='&style=element:geometry%7Ccolor:0xebe3cd&style=element:labels%7Cvisibility:off&style=element:labels.text.fill%7Ccolor:0x523735&style=element:labels.text.stroke%7Ccolor:0xf5f1e6&style=feature:administrative%7Celement:geometry%7Cvisibility:off&style=feature:administrative%7Celement:geometry.stroke%7Ccolor:0xc9b2a6&style=feature:administrative.land_parcel%7Celement:geometry.stroke%7Ccolor:0xdcd2be&style=feature:administrative.land_parcel%7Celement:labels.text.fill%7Ccolor:0xae9e90&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:landscape.natural%7Celement:geometry%7Ccolor:0xdfd2ae&style=feature:poi%7Cvisibility:off&style=feature:poi%7Celement:geometry%7Ccolor:0xdfd2ae&style=feature:poi%7Celement:labels.text.fill%7Ccolor:0x93817c&style=feature:poi.park%7Celement:geometry.fill%7Ccolor:0xa5b076&style=feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x447530&style=feature:road%7Cvisibility:off&style=feature:road%7Celement:geometry%7Ccolor:0xf5f1e6&style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:road.arterial%7Celement:geometry%7Ccolor:0xfdfcf8&style=feature:road.highway%7Celement:geometry%7Ccolor:0xf8c967&style=feature:road.highway%7Celement:geometry.stroke%7Ccolor:0xe9bc62&style=feature:road.highway.controlled_access%7Celement:geometry%7Ccolor:0xe98d58&style=feature:road.highway.controlled_access%7Celement:geometry.stroke%7Ccolor:0xdb8555&style=feature:road.local%7Celement:labels.text.fill%7Ccolor:0x806b63&style=feature:transit%7Cvisibility:off&style=feature:transit.line%7Celement:geometry%7Ccolor:0xdfd2ae&style=feature:transit.line%7Celement:labels.text.fill%7Ccolor:0x8f7d77&style=feature:transit.line%7Celement:labels.text.stroke%7Ccolor:0xebe3cd&style=feature:transit.station%7Celement:geometry%7Ccolor:0xdfd2ae&style=feature:water%7Celement:geometry.fill%7Ccolor:0xb9d3c2&style=feature:water%7Celement:labels.text.fill%7Ccolor:0x92998d'
#element:geometry%7Ccolor:0xf5f5f5&style=element:labels%7Cvisibility:off&style=element:labels.icon%7Cvisibility:off&style=element:labels.text.fill%7Ccolor:0x616161&style=element:labels.text.stroke%7Ccolor:0xf5f5f5&style=feature:administrative%7Celement:geometry%7Cvisibility:off&style=feature:administrative.country%7Celement:geometry.stroke%7Ccolor:0xe5e5e5%7Cvisibility:on%7Cweight:4.5&style=feature:administrative.land_parcel%7Celement:labels.text.fill%7Ccolor:0xbdbdbd&style=feature:administrative.neighborhood%7Cvisibility:off&style=feature:landscape%7Ccolor:0xffffff&style=feature:poi%7Cvisibility:off&style=feature:poi%7Celement:geometry%7Ccolor:0xeeeeee&style=feature:poi%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:poi.park%7Celement:geometry%7Ccolor:0xe5e5e5&style=feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&style=feature:road%7Cvisibility:off&style=feature:road%7Celement:geometry%7Ccolor:0xffffff&style=feature:road%7Celement:labels.icon%7Cvisibility:off&style=feature:road.arterial%7Celement:labels.text.fill%7Ccolor:0x757575&style=feature:road.highway%7Celement:geometry%7Ccolor:0xdadada&style=feature:road.highway%7Celement:labels.text.fill%7Ccolor:0x616161&style=feature:road.local%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&style=feature:transit%7Cvisibility:off&style=feature:transit.line%7Celement:geometry%7Ccolor:0xe5e5e5&style=feature:transit.station%7Celement:geometry%7Ccolor:0xeeeeee&style=feature:water%7Ccolor:0xdfe0ff&style=feature:water%7Celement:geometry%7Ccolor:0xe5e5e5&style=feature:water%7Celement:labels.text.fill%7Ccolor:0x9e9e9e'





for index, row in addresses.iterrows():
   
    lat = row['lat']
    long = row['long']
    #print(row['City'] + ' - ' + str(lat) + ' - ' + str(long))
    
    url = 'https://maps.googleapis.com/maps/api/staticmap?key='+apikey+'&scale='+str(scale)+'&center='+str(lat)+','+str(long)+'&zoom='+str(zoom)+'&format='+format_image+'&maptype='+maptype+''+style+'&size='+str(size_tile_x)+'x'+str(size_tile_y)
    #print(url)

    File_name = str(os.getcwd() + '\mapy\\' + row['City'] + '.png')

    # https://stackoverflow.com/questions/34692009/download-image-from-url-using-python-urllib-but-receiving-http-error-403-forbid
    r = requests.get(url,
                     stream=True, headers={'User-agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        with open(File_name, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)



