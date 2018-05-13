from selenium.webdriver.common.by import By
from models.pages import wait_clickable_element


class Login(object):
    def __init__(self, driver):
        self._driver = driver
        self._fb_email = lambda: wait_clickable_element(self._driver, 'email', by=By.NAME)
        self._fb_pwd = lambda: wait_clickable_element(self._driver, 'pass', by=By.NAME)
        self._fb_login_btn = lambda: wait_clickable_element(self._driver, 'loginbutton', by=By.ID)

    def _fill(self, elem, val):
        e = elem()
        e.click()
        e.clear()
        e.send_keys(val)

    def login_with_facebook(self, email, password):
        self._fill(self._fb_email, email)
        self._fill(self._fb_pwd, password)
        self._fb_login_btn().click()





