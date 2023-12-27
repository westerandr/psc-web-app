from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve
import os
import re
import requests

url = 'https://www.psc.gov.ws/employment/'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
downloads_directory = 'downloads'

def download_issue(issue_number: str):
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.text, 'html.parser')

  date = datetime.now()
  current_year = date.year
  current_month = date.month
  file = f"{current_year}_{issue_number}.pdf"

  res = soup.find_all("a", href=re.compile(f"/wp-content/uploads/{current_year}/{current_month}/{file}"))
  if len(res) > 0 :
    a = res[0]
    if a.text:
      link = a['href']
      file_path = f"{downloads_directory}/{file}"
      create_downloads_folder()
      if not os.path.isfile(file_path):
        urlretrieve(link, file_path)
  else:
    return None

def create_downloads_folder():
  if not os.path.exists(downloads_directory):
    os.makedirs(downloads_directory)

download_issue(48)