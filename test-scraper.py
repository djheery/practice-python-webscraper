from pprint import pp, pprint
from bs4 import BeautifulSoup
from requests_html import HTMLSession

s = HTMLSession()
url = 'https://acmegraphics.co.uk/contact/'

def getData(url):
  r = s.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  links = soup.find_all('a')
  for i in links:
    pprint(i)

soup = getData(url)