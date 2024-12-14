from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchProduct:
    def __init__(self, driver):
        self.driver = driver

        self.captcha_locator = (By.LINK_TEXT, "Anderes Bild probieren")
        self.click_popup_locator = (By.ID, "sp-cc-accept")  # Adjust to target the first product link
        self.search_field_locator = (By.ID, "twotabsearchtextbox")  # Locator for search field
        self.first_product_locator = (By.ID, "a-autoid-1-announce")  # Adjust to target the first product link

    def open_page(self, url):
        self.driver.get(url)
        time.sleep(5)

    def search(self, search_box):
        # Find the search field and send keys
        captcha = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.captcha_locator)
        )
        captcha.click()

        popup = self.driver.find_element(*self.click_popup_locator)
        popup.click()

        search_field_element = self.driver.find_element(*self.search_field_locator)
        search_field_element.send_keys(search_box)
        search_field_element.send_keys(Keys.ENTER)

        # Wait for the first product link to be clickable
        first_product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_product_locator)
        )
        first_product.click()
        time.sleep(5)  # Allow the product page to load completely