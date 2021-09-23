import requests
from bs4 import BeautifulSoup
from selenium import webdriver
PATH = "/Users/user/documents/chromedriver"
driver = webdriver.Chrome(PATH)

URL = "https://www.spotlight.com/contacts/listing/search?Category=Contacts%5CDrama%20%26%20Dance%5CChoreographers"
driver.get(URL)

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("li", class_="searchResultItem")

for result in results:
  button = result.find("a", class_="searchResultViewButton")
  print(button)
