import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "/Users/user/documents/chromedriver"
driver = webdriver.Chrome(PATH)

URL = "https://www.spotlight.com/contacts/listing/search?Category=Contacts%5CDrama%20%26%20Dance%5CChoreographers"

base_url = 'https://www.spotlight.com'

driver.get(URL)
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
button = soup.find_all("a", class_="searchResultViewButton")

links = []

def scrapeMe(l): 
  driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
  driver.get(f"{base_url}{l}")
  soup_two = BeautifulSoup(page.content, "html.parser")
  about = soup_two.find(attrs={"data-rc":"listing-About"})
  print(driver.geCurrentUrl())



for b in button:
  links.append(b.get('href'))

for link in links: 
  scrapeMe(link)