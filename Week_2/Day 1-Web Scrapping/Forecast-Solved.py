import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

page =requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.XSxJV5MzaCQ")
page
page.status_code
page.content


soup = BeautifulSoup(page.content, 'html.parser')

period_name = soup.find_all("p", class_="period-name")

forecast_item = []
for i in period_name:
   forecast_item.append(i.get_text())

short_desc = []
short = soup.find_all("p", class_="short-desc")

for j in short:
   short_desc.append((j.get_text()))

temp = soup.find_all("p", class_="temp")
temperature = []

for k in temp:
   temperature.append(k.get_text())


data = { "Forecast item": forecast_item, "Temperature": temperature, "Short description": short_desc }
df = pd.DataFrame(data)

print(df)

plt.plot( [1, 2, 3, 4], [58, 91, 71, 84] )

plt.show()