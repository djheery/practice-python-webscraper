import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

python_jobs= results.find_all(
  "h2", string=lambda text: "python" in text.lower()
  )

for job in python_jobs:
  print(job.text.strip(), end="\n"*2)
  
print(python_jobs)