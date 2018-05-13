from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from models.pages import wait_present_elements


class FacebookFriends(object):
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 5)
        self._friend = lambda: wait_present_elements(self._driver, '_698', by=By.CLASS_NAME)

    def _get_friends_list(self):
        return self._friend()

    def get_friends(self):
        num_of_loaded_friends = len(self._get_friends_list())
        while True:
            self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait.until(lambda driver: len(self._get_friends_list()) > num_of_loaded_friends)
                num_of_loaded_friends = len(self._get_friends_list())
            except:
                break
        return num_of_loaded_friends
