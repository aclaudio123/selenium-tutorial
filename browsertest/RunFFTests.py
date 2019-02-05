# Selenium 3.x requires all browsers to have separate drives.
# Firefox driver is called geckodriver
#   https://github.com/mozilla/geckodriver/releases
#

from selenium import webdriver


class RunFFTests():

    def testMethod(self):
        # Initiate the driver instance
        # Windows use "C:\\location\\geckodriver.exe"
        driver = webdriver.Firefox(
            executable_path="/Users/claudioa/Documents/libs/geckodriver")

        driver.get("http://www.letskodeit.com")


ff = RunFFTests()
ff.testMethod()
