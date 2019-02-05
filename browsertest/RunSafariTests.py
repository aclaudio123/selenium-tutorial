# Safari Automation is only possible on Mac
# please see wiki for Requirements to Run tests on safari
# https://github.com/aclaudio123/selenium-refresher/wiki/Requirements-to-run-test-on-Safari

from selenium import webdriver
import os

class RunSafariTests():
    # https://github.com/SeleniumHQ/selenium/wiki/SafariDriver
    # http://selenium-release.storage.googleapis.com/index.html

    def test(self):
        serverLocation = "/Users/claudioa/Documents/libs/selenium-server-standalone-2.53.0.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation
        # Instantiate Safari Browser Command
        driver = webdriver.Safari(quiet=True)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")


safari = RunSafariTests()
safari.test()
