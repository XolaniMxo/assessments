# -*- coding: utf-8 -*-

from behave import Given, When, Then

from pageobjects.login import LoginPageObject


@Given('the home page is open')
@When('the home page is open')
@Then('the home page is open')
def step_impl(context):
    context.current_page = LoginPageObject()
    context.current_page.open()


@Given('the user logs in with username "{username}" and password "{password}"')
@When('the user logs in with username "{username}" and password "{password}"')
@Then('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)


@Given('the user logs out')
@When('the user logs out')
@Then('the user logs out')
def step_impl(context):
    context.current_page = context.current_page.logout()


@Given('the message "{message}" is shown')
@When('the message "{message}" is shown')
@Then('the message "{message}" is shown')
@Given('the error message "{message}" is shown')
@When('the error message "{message}" is shown')
@Then('the error message "{message}" is shown')
def step_impl(context, message):
    assert message in context.current_page.message.get_message()
