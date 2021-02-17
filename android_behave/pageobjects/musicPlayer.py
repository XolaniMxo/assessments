# -*- coding: utf-8 -*-

from toolium.pageobjects.page_object import PageObject
from selenium.common.exceptions import NoSuchElementException

from toolium.pageelements import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import selenium.webdriver.support.expected_conditions as WAITCON
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from toolium.pageelements import InputText, Button
import random
import string
import time
from selenium.webdriver.common.by import By


class TabsPageObject(PageObject):
    """
    :Class represents web page elements for Login page.
    """

    def init_page_elements(self):

        """ Open page elements

        :returns: this page object instance
        """
        self.genre = Button(By.XPATH, '//*[@text="Songs by genre"]', wait=True)
        self.rock = Button(By.XPATH, '//*[@text="Rock songs"]', wait=True)
        self.song = Button(By.XPATH, '//*[@text="Silent Partner"]', wait=True)

    def SelectGenre(self):
        """ Select genre group

        :returns: this page object instance
        """
        try:
            self.logger.info("\n=====================================Genre======================================")
            self.logger.debug("Opening genres")
            self.logger.debug("Checking if the button is present : %s", self.genre)
            self.logger.debug("\n-----------------------------------------------------------------------------------")

            self.genre.wait_until_visible()
            self.genre.click()
            time.sleep(2)
            return True
        except NoSuchElementException:
            self.logger.debug("error", "Element {} does not exist".format(self.genre))
            return None

    def Rock(self):
        """ Select Rock music genre

        :returns: this page object instance
        """
        try:
            self.logger.info("\n===============================Selecting Rock music from genre=================================")
            self.logger.debug("Choose a genre")
            self.logger.debug("Checking if the pageElement is present : %s", self.rock)
            self.logger.debug("\n-----------------------------------------------------------------------------------")

            self.rock.wait_until_visible()
            self.rock.click()
            time.sleep(2)
            return True
        except NoSuchElementException:
            self.logger.debug("error", "Element {} does not exist".format(self.rock))
            return None

    def SelectedSong(self):
        """ Select play selected song

        :returns: this page object instance
        """
        try:
            self.logger.info("\n===============================Playing awakening=================================")
            self.logger.debug("Playing song.")
            self.logger.debug("Checking if the pageElement is present : %s", self.song)
            self.logger.debug("\n-----------------------------------------------------------------------------------")

            self.song.wait_until_visible()
            self.song.click()
            time.sleep(10)
            return True
        except NoSuchElementException:
            self.logger.debug("error", "Element {} does not exist".format(self.song))
            return None
