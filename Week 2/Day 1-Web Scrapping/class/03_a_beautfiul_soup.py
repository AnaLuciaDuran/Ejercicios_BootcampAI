# https://www.dataquest.io/blog/python-api-tutorial/

import requests
from bs4 import BeautifulSoup

# Make a get request to get the latest position of the international space station from the opennotify api.
page =requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
# Print the status code of the response.

soup =BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

print()
print("This are the children")
print()

html = list(soup.children)[2]

body= list(html.children)[3]

p = list(body.children)[1]

print(p.get_text())

#Faster Way

p = soup.find('p')

print(p)

