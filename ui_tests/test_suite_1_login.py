import pytest
from selenium import webdriver
from models.pages import Login, FacebookFriends
#provide DRIVER_PATH, DRIVER_PATH(user whose friends must be counted) and credentials to login
DRIVER_PATH = ''
URL = 'https://www.facebook.com/'
NICKNAME = ''
EMAIL = ''
PASSWORD = ''


@pytest.yield_fixture(scope='module', autouse=True)
def chrome_driver(request):
    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.set_window_size(1920, 1080)
    if request.module is not None:
        request.module.driver = browser
    yield browser
    browser.quit()

driver = chrome_driver(True)


def test_count_friends():
    driver.get(URL)
    l=Login(driver)
    l.login_with_facebook(email=EMAIL, password=PASSWORD)
    driver.get(URL + '{}/friends'.format(NICKNAME))
    f=FacebookFriends(driver)
    f.get_friends()

