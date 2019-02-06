# Browser Interaction and Navigating Web Pages
#
from selenium import webdriver


class BrowserInteraction:
    def test(self):
        baseUrl = "https://claudioasangong.com/"
        driver = webdriver.Chrome()

        # Maximize browser Window before getting webpage
        driver.maximize_window()

        # Open the URL
        driver.get(baseUrl)

        # Get title of page
        title = driver.title
        print("Title of web page:", title)

        # Get Current URL
        currentURL = driver.current_url
        print('Current URL of web page is:', currentURL)

        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print('Browser Refreshed 2nd time')

        # Open another URL
        driver.get('https://claudioasangong.com/category/projects/')
        print('New URL is:', driver.current_url)

        # Browser Back
        driver.back()
        print('Go one step back in browser history')
        print('URL went back to:', driver.current_url)

        # Browser Forward
        driver.forward()
        print('Go one step forward in browser history')
        print('Now current url is:', driver.current_url)

        # Get Page source
        pagesource = driver.page_source
        print(pagesource)

        # Browser close/quit
        # driver.close()
        driver.quit()


BI = BrowserInteraction()
BI.test()






