
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from pprint import pprint

s = HTMLSession()
base_url = 'https://spotlight.com'
url = 'https://www.spotlight.com/contacts/listing/search?Category=Contacts%5CDrama%20%26%20Dance%5CChoreographers'

def get_data(url):
  r = s.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  return soup
  
def get_about_info(about):
  txt = ''
  if about != None:
    if len(about) > 1:
      arr = about.find_all('p')
      for p in arr: 
        txt += p.text.strip()
    else:
      txt = about.find('p').text.strip()
  else:
    txt = 'Not Defined'
  return txt

def unscramble_email(email):
  return 'email@email.com'

def get_targeted_content(page):
  name = page.find('span', {'data-rc': 'listing-Name'})
  about = page.find('span', {'data-rc': 'listing-About'})
  email = page.find('a', {'data-rc': 'listing-body-Email address'})
  website = page.find('a', {'data-rc': 'listing-body-Website'})

  return {
    'name': name.text.strip(),
    'website': website.get('href'),
    'email': unscramble_email(email),
    'about': get_about_info(about)
  }

def get_links(s): 
  linkArr = []
  links = s.find_all('a', {'class': 'searchResultViewButton'})
  for link in links:
    linkArr.append(link.get('href'))
  
  return  linkArr

def get_scraping(links):
  data = []
  for link in links:
    page = get_data(f'{base_url}{link}')
    target_content = get_targeted_content(page)
    data.append(target_content)
  return data


soup = get_data(url)
links = get_links(soup)
content = get_scraping(links)

pprint(content)

  
