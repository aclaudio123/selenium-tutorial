from selenium import webdriver
import os

class RunIETestsWindows():

    def test(self):
        driverLocation = "C:\\Users\\claudioa\\Documents\\libs\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverLocation
        driver = webdriver.Ie(driverLocation)
        driver.get("http://www.letskodeit.com")


IEbrowser = RunIETestsWindows()
IEbrowser.test()
