import pandas as pd
import plotly.express as px
import plotly.offline as py

# Collecting covid data

githubdata_url = 'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(githubdata_url)
#print(df.head())

# Creating chloropleth animation
fig = px.choropleth(df , locations = 'Country', locationmode = 'country names', color = 'Confirmed',animation_frame = 'Date')
fig.update_layout(title_text = 'The spread of Covid19 throughout the World')

py.offline.plot(fig, filename='Global_CovidSpread.html' )
