from bs4 import BeautifulSoup
import lxml
from property_renting_bot.constants import SCRAPPED_URL
import requests


class PropertyScraper:

    def __init__(self):
        self.url = SCRAPPED_URL
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, "lxml")

        self.address_list = []
        self.price_list = []
        self.url_list = []


    def print_html(self):
        print(self.soup.prettify())

    def scrape_data(self) -> None:
        property_cards = self.soup.find_all("article", {"data-test" : "property-card"})

        for card in property_cards:
            address = card.find("address").get_text().strip()
            # Use the formatted_price variable as the final processed data
            price = card.find("span", {"data-test" : "property-card-price"})
            price = price.get_text().split("+")[0] if "+" in price.get_text() else price.get_text().split("/")[0]
            url = card.find("a", {"data-test" : "property-card-link"}).get("href")

            # print(price)
            # print(address)
            # print(url)

            self.address_list.append(address)
            self.price_list.append(price)
            self.url_list.append(url)








