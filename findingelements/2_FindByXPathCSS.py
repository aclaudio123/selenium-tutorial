# Finding DOM elements using XPath and CSS selector
# please see wiki for XPath and CSS selector cheat sheet

from selenium import webdriver


class FindByXPathCSS():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("We found an element by XPATH")

        elementByCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementByCSS is not None:
            print("We found an element by CSS")


ff = FindByXPathCSS()
ff.test()
