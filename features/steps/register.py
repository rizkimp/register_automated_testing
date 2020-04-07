import strgen #library to generate random string
from selenium import webdriver
from behave import *
from locators import *
from selenium.webdriver.common.by import By
from time import sleep

@given(u'prepare to register')
def step_impl(context):
    context.browser.implicitly_wait(30)
    context.browser.find_element(By.XPATH,locator.navbar)
    context.browser.implicitly_wait(30)
    context.browser.find_element(By.XPATH,locator.slide)

@when(u'input valid data')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.button_register1).click()
    sleep(1)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.form_register)
    sleep(1)
    #generate random string for uniq username and email
    username = strgen.StringGenerator("[\w\d]{5}").render()
    email = "@email.automation"
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_email).send_keys("%s%s" % (username,email))
    sleep(1)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_username).send_keys("%s" % (username))
    sleep(1)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_password1).send_keys("12345678wasd")
    sleep(1)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.input_password2).send_keys("12345678wasd")
    sleep(1)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.button_register2).click()
    sleep(3)

@then(u'success register')
def step_impl(context):
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.navbar)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.avatar_plain)
    context.browser.implicitly_wait(10)
    context.browser.find_element(By.XPATH,locator.slide)
