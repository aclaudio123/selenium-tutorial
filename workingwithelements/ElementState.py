# How to find if an element is enabled or disabled
# disable elements have attribute disabled= in them

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState:
    def isEnabled(self):
        base_url = 'http://www.google.com'
        driver = webdriver.Chrome()
        driver.get(base_url)
        # wait for all elements to load
        driver.implicitly_wait(3)

        # True for is_enabled(), false if element has attribute disable=
        ele = driver.find_element(By.NAME, 'q')
        state = ele.is_enabled()
        print('Element is Enabled?', state)

        ele.send_keys("letskodeit")
        time.sleep(3)


browser = ElementState()
browser.isEnabled()
