from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
url = "https://www.rappler.com"

# Send a request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


news_container = soup.find_all("h3", attrs={"class": "post-card__secondary-title"})


for container in news_container:
    headline_title = container.find("a")



    if headline_title:
        href = headline_title.get("href")
        print(f"HeadLine Title:  {headline_title.text}")
        print(f"Link: {href}")

