# Download the chromedriver and add to your system path
# or put in a directory and pass location as string
#   http://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver


class RunChromeTests:
    def test(self):
        # Windows use "C:\\location\\geckodriver.exe"
        driver_location = '/Users/claudioa/Documents/libs/chromedriver'
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driver_location)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")


browser = RunChromeTests()
browser.test()
