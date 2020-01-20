


#### test 1

import os
os.chdir('D:\KK\OneDrive\Wroclaw w Liczbach\Gotowe projekty\\20191219 zielone miasta')
os.getcwd()

with open(os.getcwd() + '\\apikey.txt') as f:
    apikey = f.readline()
    f.close


from googlemaps import Client as GoogleMaps
import pandas as pd 
import gmaps
gmaps.__version__

# Wcyztanie miast z pliku i ciągnięcie dla nich koordynatów
# https://towardsdatascience.com/how-to-generate-lat-and-long-coordinates-from-an-address-column-using-pandas-and-googlemaps-api-d66b2720248d

addresses = pd.read_csv(os.getcwd() + '\\Adresy miast bez polskich znakow.csv', sep = ';')

addresses['long'] = ""
addresses['lat'] = ""

gmaps_api = GoogleMaps(apikey)

for x in range(len(addresses)):
    geocode_result = gmaps_api.geocode(addresses['City'][x])
    addresses['lat'][x]  = geocode_result[0]['geometry']['location']['lat']
    addresses['long'][x] = geocode_result[0]['geometry']['location']['lng']
addresses.head()

#zapis do pliku
addresses.to_csv("addresses_coord 2.csv", index=False)
