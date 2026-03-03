import sys
import requests
from bs4 import BeautifulSoup


#SCRAPER CODE FOR HTML BODY,TITLE AND LINKS

if len(sys.argv) == 2:
    url = sys.argv[1]
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()
    print("Links:")
    for link in soup.find_all('a'):
        print(link.get('href'))
    print("Title:")
    if soup.title:
        print(soup.title.text)
    print("Body:")
    if soup.body:
        print(soup.body.get_text(separator="\n", strip=True))

else:
    print("Invalid Input")
