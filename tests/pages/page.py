from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.variables import GOOGLE_SEARCH_URL
from tests.locators import GoogleSearchLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def check_element_is_displayed(self, locator):
        element = self.find_element(locator)
        element.is_displayed()


class GoogleSearchPage(BasePage):

    def go_to_site(self, url=GOOGLE_SEARCH_URL):
        self.driver.get(url)

    def perform_search(self, phrase):
        search_input = self.find_element(GoogleSearchLocators.GOOGLE_SEARCH_FIELD)
        search_input.send_keys(phrase + Keys.RETURN)

    def get_links_from_search_results(self):
        search_results = self.find_elements(GoogleSearchLocators.GOOGLE_SEARCH_RESULTS)
        links = []
        for link in search_results:
            links.append(link.get_attribute('href'))
        return links


