import folium
from folium.plugins import MarkerCluster
import csv
import os
from geopy import geocoders
import time
import webbrowser

gmrMap = folium.Map(location=[39, -77], zoom_start = 5)
type(gmrMap)

marker_cluster = MarkerCluster().add_to(gmrMap)

Bing_Key = 'Ag0T3odWUsHkFyVhp8Lw8oruQo1tsWUw1PuHC_yiiy3edtmXnWZ2WMKHob6504ZL'
g = geocoders.Bing(Bing_Key)

CSV_File = 'geoloc.csv'

csvReader = csv.DictReader(open(CSV_File), delimiter = ',', quotechar='"')

contacts = [row for row in csvReader]

for c in contacts:
    gmr = g.geocode(c['Location'], exactly_one = True, timeout = 4.1)
    
    if gmr == []:
        continue
    
    folium.Marker([gmr[1][0], gmr[1][1]], popup = c['Company']).add_to(marker_cluster)
    
outfile = 'gmr' + str(time.time()).replace(".","l") + ".html"
gmrMap.save(outfile)
webbrowser.open(outfile)