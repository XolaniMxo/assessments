# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject
import time


class SecureAreaPageObject(PageObject):
    """
    :Class represents web page elements for Login page.
    """
    def init_page_elements(self):
        """ Initialize web page elements using element locator.

        :locate: loactes page lelements
        """
        self.message = MessagePageObject()
        self.logout_button = Button(By.XPATH, "//div[@id='content']//a[contains(@class,'button')]")

    def logout(self):
        """ Log out of secure area

        :returns: login page object instance
        """
        from pageobjects.login import LoginPageObject

        self.logger.debug("===============================Logging out==================================")
        self.logger.debug("Clicking logout button")
        time.sleep(2)
        self.logout_button.click()
        return LoginPageObject(self.driver_wrapper).wait_until_loaded()
