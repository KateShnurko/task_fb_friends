from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

SECONDS_TO_WAIT=10

def wait_visible_element(driver, locator, by=By.XPATH, seconds_to_wait=SECONDS_TO_WAIT):
    return WebDriverWait(driver, seconds_to_wait).until(
        EC.visibility_of_element_located((by, locator)),
        'element: "%s" was not found or was not visible during %i seconds' % (locator, seconds_to_wait))


def wait_clickable_element(driver, locator, by=By.XPATH, seconds_to_wait=SECONDS_TO_WAIT):
    return WebDriverWait(driver, seconds_to_wait).until(
        EC.element_to_be_clickable((by, locator)),
        'element: "%s" was not found or was not visible during %i seconds' % (locator, seconds_to_wait))


def wait_present_element(driver, locator, by=By.XPATH, seconds_to_wait=SECONDS_TO_WAIT):
    return WebDriverWait(driver, seconds_to_wait).until(
        EC.presence_of_element_located((by, locator)),
        'elements: "%s" was not found or was not visible during %i seconds' % (locator, seconds_to_wait))


def wait_present_elements(driver, locator, by=By.XPATH, seconds_to_wait=SECONDS_TO_WAIT):
    return WebDriverWait(driver, seconds_to_wait).until(
        EC.presence_of_all_elements_located((by, locator)),
        'elements: "%s" was not found or was not visible during %i seconds' % (locator, seconds_to_wait))
