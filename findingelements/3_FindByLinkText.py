# Finding DOM elements using Link text and partial link text
# i.e. the complete or partial text inside an archor tag
# <a href=""> Link Text </a>

from selenium import webdriver


class FindByLinkText():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByLinkText = driver.find_element_by_link_text("Login")

        if elementByLinkText is not None:
            print("We found an element by Link Text")

        # find element using a partial link text
        elementByPartialLinkText = driver.find_element_by_partial_link_text("Pract")

        if elementByPartialLinkText is not None:
            print("We found an element by Partial Link Text")


ff = FindByLinkText()
ff.test()
