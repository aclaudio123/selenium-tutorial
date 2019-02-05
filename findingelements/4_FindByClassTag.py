# Finding DOM elements using class attribute
# class is an attribute of any html element
# Note: it's not a good idea to find by class name
# since class names are mostly not unique to a particular element
# Same with finding elements by Tag Name
# Always try to use attributes that are unique to an element
# except in cases were need to find multiple elements

from selenium import webdriver


class FindByClassTag():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)

        elementByClassName = driver.find_element_by_class_name("displayed-class")
        elementByClassName.send_keys("Testing The Element")

        if elementByClassName is not None:
            print("We found an element by Class Name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text

        if elementByTagName is not None:
            print("We found an element by Tag Name and the text on element is: " + text)


ff = FindByClassTag()
ff.test()
