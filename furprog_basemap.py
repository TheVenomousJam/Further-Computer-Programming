import json
import folium
import requests
import mimetypes
import http.client
import pandas as pd
import webbrowser
from folium.plugins import HeatMap
from pandas.io.json import json_normalize


#Collecting world covid data - Continuously updating

connect =  http.client.HTTPSConnection("api.covid19api.com")
payload = ' '
headers = { }
connect.request("GET","/summary",payload,headers)
res = connect.getresponse()
data = res.read().decode('UTF-8')

covid_data = json.loads(data)

pd.json_normalize(covid_data['Countries'],sep=',')
#print(covid_data)

df = pd.DataFrame(covid_data['Countries'])
#print(df)

covid_data2 = df.drop(columns = ['CountryCode','Slug','ID','Date','Premium'],axis=1)
#print(covid_data2)

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes=f'{url}/world-countries.json'
geo_json_data = json.loads(requests.get(country_shapes).text)

covid_data2.update(covid_data2['TotalConfirmed'].map('Total Confirmed:{}'.format))
covid_data2.update(covid_data2['TotalRecovered'].map('Total Recovered:{}'.format))


#Collecting world coordinates

co_ordinates = pd.read_csv('world_coordinates.csv', sep = ',')
co_ordinates.head()
co_ordinates2 = co_ordinates.drop(columns = ['Code'],axis=1)

print(co_ordinates2)

covid_final = pd.merge(covid_data2,co_ordinates2,on ='Country')


#Creating base folium map

map1 = folium.Map(tiles='StamenToner', max_bounds=True, min_zoom=2.5)

deaths = covid_final['TotalDeaths'].astype(float)
lat = covid_final['latitude'].astype(float)
lon = covid_final['longitude'].astype(float)
map1.add_child(HeatMap(zip(lat,lon,deaths),radius=0))

def Axis(point):
    folium.CircleMarker(location=[point.latitude,point.longitude],
                       radius=5,
                       weight=2,
                       popup=[point.Country,point.TotalDeaths],
                       fill_color='#000000').add_to(map1)
    
covid_final.apply(Axis,axis=1)
map1.fit_bounds(map1.get_bounds())

map1.save('map1.html')
webbrowser.open('map1.html')
    