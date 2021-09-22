import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")
for job_elem in job_elements:
    title_element = job_elem.find("h2", class_="title")
    company_element = job_elem.find("h3", class_="company")
    location_element = job_elem.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip(), "\n"*2)
    