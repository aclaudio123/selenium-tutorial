# Working with Radio buttons and checkboxes
# Only one Radio button can be selected at a time
# Multiple checkboxes can be selected at any given time
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class RadioButtonsAndCheckboxes:
    def __init__(self):
        self.base_url = "https://letskodeit.teachable.com/pages/practice"
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)

    def test_radio_btn(self):

        # Only one Radio Button can be selected at a time

        bmwRadioBtn = self.driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)
        benzRadioBtn = self.driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)
        hondaRadioBtn = self.driver.find_element_by_id("hondaradio")
        hondaRadioBtn.click()

        time.sleep(2)
        print("BMW Radio Button is Selected?", bmwRadioBtn.is_selected())
        print("Benz Radio Button is Selected?", benzRadioBtn.is_selected())
        print("Honda Radio Button is Selected?", hondaRadioBtn.is_selected())

    def test_check_boxes(self):

        # Multiple checkboxes can be selected
        bmw_check_box = self.driver.find_element(By.ID, 'bmwcheck')
        bmw_check_box.click()

        time.sleep(2)
        benz_check_box = self.driver.find_element(By.ID, 'benzcheck')
        benz_check_box.click()

        time.sleep(2)
        honda_check_box = self.driver.find_element(By.ID, 'hondacheck')
        honda_check_box.click()

        print("BMW checkbox is Selected?", bmw_check_box.is_selected())
        print("Benz checkbox is Selected?", benz_check_box.is_selected())
        print("Honda checkbox is Selected?", honda_check_box.is_selected())

    def browser_quit(self):
        self.driver.quit()


tt = RadioButtonsAndCheckboxes()
tt.test_radio_btn()
tt.test_check_boxes()
tt.browser_quit()