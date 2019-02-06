# Clicking links and typing text on a web page

from selenium import webdriver
from selenium.webdriver.common.by import By


class ClickAndSendKeys:
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)

        # wait for all elements to be found or command to complete
        # before next step
        driver.implicitly_wait(10)

        login_link = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_link.click()

        email_address = driver.find_element(By.ID, "user_email")
        email_address.send_keys('test')

        password_field = driver.find_element(By.ID, "user_password")
        password_field.send_keys('test')

        # clear the email element
        email_address.clear()
        email_address.send_keys('test')

        password_field.clear()
        password_field.send_keys('test')


click_send_keys = ClickAndSendKeys()
click_send_keys.test()







