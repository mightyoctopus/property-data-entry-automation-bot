import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium_stealth import stealth
import time

import property_renting_bot.constants as const

class FormAutoFiller:
    def __init__(self, address, price, url ,**kwargs):
        options = uc.ChromeOptions()
        options.add_argument("--disable=popup-blocking")

        self.driver = uc.Chrome(options=options, enable_cdp_events=True, **kwargs)

        stealth(
            self.driver,
            vendor="Google Inc.",
            platform="MacIntel",
            webgl_vendor="Apple Inc.",
            renderer="Apple M1",
            fix_hairline=True,
        )

        self.driver.implicitly_wait(2)
        # Additional JavaScript stealth injection
        self.driver.execute_script("""
                    Object.defineProperty(navigator, 'plugins', {
                        get: function() {
                            return [1, 2, 3, 4, 5];
                        },
                    });
                """)

        self.driver.get(const.AUTO_FILLING_URL)
        # self.question_boxes_element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_all_elements_located((By.XPATH, '//div[@role = "listitem"]'))
        # )
        self.address = address
        self.price = price
        self.url = url


    def submit_form(self, index:int):

        time.sleep(1)

        address_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@aria-describedby="i2 i3"]'))
               )
        address_field.click()
        address_field.send_keys(self.address[index])

        time.sleep(0.5)
        price_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@aria-describedby="i7 i8"]'))
                )
        price_field.click()
        price_field.send_keys(self.price[index])

        time.sleep(0.5)
        url_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@aria-describedby="i12 i13"]'))
                )
        url_field.click()
        url_field.send_keys(self.url[index])

        time.sleep(0.5)
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Submit"]'))
        )
        submit_btn.click()
        print(f"Submission[{index}] has been submitted!")

    def move_onto_next_form(self):
        another_form_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "https://docs.google.com/forms")]'))
        )
        another_form_btn.click()



