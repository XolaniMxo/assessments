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
from behave import Given, When, Then
from android_behave.pageobjects.musicPlayer import TabsPageObject


@Given('the menu is open')
@When('the menu is open')
@Then('the menu is open')
def step_impl(context):
    context.current_page = TabsPageObject()


@Given('the user goes to genres')
@When('the user goes to genres')
@Then('the user goes to genres')
def step_impl(context):
    context.current_page = TabsPageObject()
    context.current_page.SelectGenre()


@Given('the user chooses Rock')
@When('the user chooses Rock')
@Then('the user chooses Rock')
def step_impl(context):
    context.current_page = TabsPageObject()
    context.current_page.Rock()


@Given('the user plays Awakening and closes the application')
@When('the user plays Awakening and closes the application')
@Then('the user plays Awakening and closes the application')
def step_impl(context):
    context.current_page = TabsPageObject()
    context.current_page.SelectedSong()