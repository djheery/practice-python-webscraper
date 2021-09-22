import requests
import webbrowser
from bs4 import BeautifulSoup

URL = "https://www.spotlight.com/contacts/listing/search?Category=Contacts%5CDrama%20%26%20Dance%5CChoreographers"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("li", class_="searchResultItem")

print(len(results))
for result in results:
  name = result.find('a', class_="searchResultTitle")
  occupation = result.find('div', class_="searchResultCategories")
  print(name.text.strip(), end="\n")
  print(occupation.text.strip(), end="\n"*2)


