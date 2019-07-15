# https://www.dataquest.io/blog/python-api-tutorial/

import requests
from bs4 import BeautifulSoup

# Make a get request to get the latest position of the international space station from the opennotify api.
page =requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# Print the status code of the response.

soup =BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

# outer = soup.find_all('p', class_='outer-text')
outer = soup.find(id='first').string
print(outer)
