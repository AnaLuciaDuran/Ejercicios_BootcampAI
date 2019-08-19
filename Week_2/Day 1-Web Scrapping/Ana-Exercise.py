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
#print(soup.prettify())

main =list(soup.children)[2].body.main.div

div = list(soup.find(id="seven-day-forecast-list"))

image_text = [d.find("img", alt=True) for d in div]

alt_text = []
long_description = []
period_name = []

for d in image_text:
   alt_text.append(d['alt'])

for a in alt_text:
   period_name.append(a.split(":")[0])
   long_description.append(a.split(":")[1])



short_description = [d.find("p", class_="short-desc").get_text() for d in div]

temperature = [d.find("p", class_="temp").get_text() for d in div]

data = { "Forecast item": period_name, "Temperature": temperature, "Short description": short_description, "Long description": long_description}

df = pd.DataFrame(data)
print(df)


#just_low = [ int(t.split()[1]) if t.startswith("L") for t in temperature]

#plt.plot(period_name, )
#plt.show()
w = 4
h = 3
d = 70
plt.figure(figsize=(w, h), dpi=d)
x1 = (period_name)
y1 = (temperature)
plt.plot(x1, y1)

x2 = (period_name)
y2 = (temperature)
plt.plot(x2, y2)
plt.savefig("out.png")