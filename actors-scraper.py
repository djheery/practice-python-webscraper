from requests_html import HTMLSession
from bs4 import BeautifulSoup
from pprint import pp, pprint

s = HTMLSession()
base_url = 'https://spotlight.com'
url = 'https://www.spotlight.com/contacts/listing/search?query=Actors'

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
    txt = 'No about content provided'
  return txt

def check_pagination(page):
  return

def unscramble_email(email):
  email = email.text.strip()
  unscrambled_email = ''
  pointer = 1
  max_pointer = 6
  i = 0
  while i < len(email):
    if i >= pointer and i <= max_pointer :
      i = i + 5
      pointer = max_pointer + 2
      max_pointer = pointer + 5
    else:
      unscrambled_email += email[i]  
    i = i + 1
  return unscrambled_email

def check_address(page):
  if not page.find('div', {'data-rc': 'listing-body-address'}):
    return 'No Address Stated'
  else:
    address_container = page.find('div', {'data-rc': 'listing-body-address'})
    address = address_container.find_all('span')
    return address[1].text.strip()

def get_website(website):
  if website == None:
    return 'No Website Found'
  else: 
    website = website.get('href')
    return website
  

def get_targeted_content(page):
  name = page.find('span', {'data-rc': 'listing-Name'})
  about = page.find('span', {'data-rc': 'listing-About'})
  email = page.find('a', {'data-rc': 'listing-body-Email address'})
  website = page.find('a', {'data-rc': 'listing-body-Website'})
  address = check_address(page)

  return {
    'name': name.text.strip(),
    'website': get_website(website),
    'email': unscramble_email(email),
    'about': get_about_info(about),
    'address': address
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