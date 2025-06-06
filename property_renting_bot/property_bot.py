from property_renting_bot.form_auto_filler import FormAutoFiller
from property_renting_bot.property_scraper import PropertyScraper
import time

class PropertyBot:

    def __init__(self):
        self.scraper = PropertyScraper()
        self.n = 0


    def run_scraping(self):
        self.scraper.scrape_data()
        print("ADDRESS LIST: ", self.scraper.address_list[0])
        # print(self.scraper.price_list)
        # print(self.scraper.url_list)

    def run_auto_filler(self):
        auto_filler = FormAutoFiller(
            address=self.scraper.address_list,
            price=self.scraper.price_list,
            url=self.scraper.url_list
        )

        while self.n < len(self.scraper.address_list):
            time.sleep(1)
            auto_filler.submit_form(self.n)
            time.sleep(1)
            auto_filler.move_onto_next_form()
            self.n += 1



