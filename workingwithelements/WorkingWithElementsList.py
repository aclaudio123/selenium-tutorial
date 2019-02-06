# getting multiple elements with same attribute values

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class WorkingWithElementsList:
    def test(self):
        base_url = "https://letskodeit.teachable.com/pages/practice"
        driver =  webdriver.Chrome()
        driver.get(base_url)

        # wait for all elements to load
        driver.implicitly_wait(3)

        radio_btn_list = driver.find_elements(By.XPATH,
                                              "//input[contains(@name, 'cars') and contains(@type, 'radio')]")

        print('Number of elements is', len(radio_btn_list))

        for radio_btn in radio_btn_list:
            isSelected = radio_btn.is_selected()
            if not isSelected:
                radio_btn.click()
        time.sleep(2)
        driver.quit()


tt = WorkingWithElementsList()
tt.test()
