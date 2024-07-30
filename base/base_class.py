import datetime
import time

from selenium.webdriver import ActionChains, Keys


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Getting current URL Method"""

    def get_current_url(self):
        """URL verification Method"""
        get_url = self.driver.current_url
        print("current url " + get_url)

    """WORD assertion Method"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Value of word is GOOD')

    """Screenshot Method"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\Dasha\\PycharmProjects\\python_my_project\\screen\\' + name_screenshot)
        print('Screenshot of final step is made')

    """URL assertion Method"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Value of URL is GOOD')

    """Scroll page Method"""
    def scroll_page(self, pixels):  # Scroll page with specified pixels
        self.driver.execute_script(f'window.scrollBy(0, {pixels})')
        print(f'Screen is scrolled by {pixels} pixels')

    """Clear and input Method"""
    def clear_and_input(self, element, value):  # Clear and input value using ActionChains
        actions = ActionChains(self.driver)
        actions.click(element).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
            Keys.DELETE).send_keys(value).perform()
