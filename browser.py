from selenium import webdriver

class Browser:
    browser = webdriver.Chrome()
    browser.maximize_window()
    # time.sleep(2)
    def close(self):
        self.browser.quit()



'''
Din sesiunea online

from selenium import webdriver


class Browser:
    browser = webdriver.Chrome()
    browser.maximize_window()

    def close(self):
        self.browser.quit()

'''
