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
import logging
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject

from pageobjects.secure_area import SecureAreaPageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time

class LoginPageObject(PageObject):
    """
    :Class represents web page elements for Login page.
    """

    def init_page_elements(self):
        """ Initialize web page elements using element locator.

        :locate: loactes page lelements
        """
        self.page_tittle = PageElement(By.CLASS_NAME, 'example', wait=True) 
        self.username = InputText(By.ID, 'username', wait=True)
        self.password = InputText(By.ID, 'password', wait=True)
        self.login_button = Button(By.XPATH, "//form[@id='login']/button", wait=True)
        self.login_message = MessagePageObject(wait=True)
        self.welcome_page_message = PageElement(By.CLASS_NAME, 'subheader', wait=True)

    def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        self.logger.debug("===============================Openining Page=======================================")
        self.driver.get('{}/login'.format(self.config.get('Test', 'landing_page')))
        return self

    def wait_until_loaded(self):
        """ Wait until login page is loaded

        :returns: this page object instance
        """
        self.logger.debug("===============================Loading Page Objects==================================")
        self.username.wait_until_visible()
        return self

    def login(self, user):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.logger.debug("Login with user '%s'", user['username'])

        self.logger.debug("Inputing Username")
        self.username.text = user['username']

        self.logger.debug("Inputing password")
        self.password.text = user['password']
        self.login_button.wait_until_visible()

        self.logger.debug("===============================Clicking Login button==================================")
        time.sleep(2)
        self.login_button.click()
        return SecureAreaPageObject(self.driver_wrapper)
