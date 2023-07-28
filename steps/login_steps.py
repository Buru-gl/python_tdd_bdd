from behave import *


@given('I am on the login page https://demo.nopcommerce.com/login')
def step_impl(context):
    context.login_page.navigate_to_login()


@when(u'I insert an unregistered email in the email field')
def step_impl(context):
    context.login_page.enter_email()


@when(u'I insert a password')
def step_impl(context):
    context.login_page.enter_password()


@when(u'I click on login button')
def step_impl(context):
    context.login_page.click_login_button()


@then(
    u'I get the following message Login was unsuccessful. Please correct the errors and try again. No customer account found')
def step_impl(context):
    assert context.login_page.is_error_message_displayed()


"""
Din clasa, sesiune online-
from behave import *


@given('I am on the login page https://demo.nopcommerce.com/login')
def step_impl(context):
    context.login_page.navigate_to_login()

@when(u'I insert an unregistered email in the email field')
def step_impl(context):
    context.login_page.enter_email()

@when(u'I insert a password')
def step_impl(context):
    context.login_page.enter_password()

@when(u'I click on login button')
def step_impl(context):
     context.login_page.click_login_button()


@then(u'I get the following message Login was unsuccessful. Please correct the errors and try again. No customer account found')
def step_impl(context):
    assert context.login_page.is_error_message_displayed()
"""
