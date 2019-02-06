# working with displayed or hidden elements

from selenium import webdriver
from selenium.webdriver.common.by import By


class HiddenElements:

    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Chrome()
        driver.get(base_url)
        driver.implicitly_wait(5)

        text_box = driver.find_element(By.ID, 'displayed-text')

        # check if text box is displayed on page
        if text_box.is_displayed():
            print("Text box is visible?", text_box.is_displayed())
            print("Now clicking the Hide button...")
            driver.find_element(By.ID, 'hide-textbox').click()
            print("Text box is now visible?", text_box.is_displayed())
        else:
            # click the show button
            print("Text box is visible?", text_box.is_displayed())
            driver.find_element(By.ID, 'show-textbox').click()
            print("Now clicking the Show button...")
            print("Text box is now visible?", text_box.is_displayed())

        driver.quit()


tt = HiddenElements()
tt.test()
