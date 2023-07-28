import time

from selenium.webdriver.common.by import By

from browser import Browser



class LoginPage(Browser):
    E_LOCATOR = (By.ID, 'Email')
    P_LOCATOR = (By.ID, 'Password')
    URL = 'https://demo.nopcommerce.com/login'
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[class="button-1 login-button"]')
    ERROR_LOCATOR = (By.CLASS_NAME, "message-error")


    def enter_email(self):
        self.browser.find_element(*self.E_LOCATOR).send_keys('itf@email.fr')

    def navigate_to_login(self):
        self.browser.get(self.URL)

    def enter_password(self):
        self.browser.find_element(*self.P_LOCATOR).send_keys('A1234')

    def click_login_button(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
        print(self.browser.find_element(*self.ERROR_LOCATOR).text)


    def is_error_message_displayed(self):
        return self.browser.find_element(*self.ERROR_LOCATOR).is_displayed()
