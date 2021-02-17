# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
import time


class MessagePageObject(PageObject):
    """
    :Class represents web page elements for Login page.
    """
    def init_page_elements(self):
        """ Initialize web page elements using element locator.

        :locate: loactes page lelements
        """
        self.message = Text(By.XPATH, '//*[@id="flash"]')

    def get_message(self):
        """ Get first line of actual message

        :returns: str with message
        """
        self.logger.debug("===============================Getting assert message==================================")
        time.sleep(3)
        return self.message.wait_until_visible(5).text.splitlines()[0]
