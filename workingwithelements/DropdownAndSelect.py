# How to work with a dropdown menu
# Not all elements that look like a dropdown are dropdowns
# A proper dropdown element should have a <select> tag
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropdownAndSelect:
    def test(self):
        base_url = "http://www.expedia.com"
        driver = webdriver.Chrome()
        driver.get(base_url)

        dropdown = driver.find_element(By.ID, 'package-advanced-preferred-class-hp-package')

        dropdown_menu = Select(dropdown)

        # Select class has 3 methods
        # 1. select using attribute value=
        print("Select First class by value", dropdown_menu.select_by_value('f'))
        time.sleep(2)

        # 2. select using index
        dropdown_menu.select_by_index(1)
        print("Select Business by index")
        time.sleep(2)

        # 3. select using visible text
        dropdown_menu.select_by_visible_text('Premium economy')
        print("Select Premium economy")
        time.sleep(2)

        # select Economy/Coach
        dropdown_menu.select_by_index(3)
        print("Select Economy/Coach by index")
        time.sleep(2)

        driver.quit()


tt = DropdownAndSelect()
tt.test()
