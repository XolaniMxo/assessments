# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
