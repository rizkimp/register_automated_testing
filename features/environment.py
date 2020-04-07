from selenium import webdriver
from time import sleep

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    context.browser = webdriver.Chrome(executable_path='../features/browsers/chromedriver',chrome_options=options)
    #context.browser = webdriver.Chrome('../features/browsers/chromedriver')
    context.browser.set_window_size(1440,900)
    url = context.config.userdata.get("url")
    context.browser.get(url)

def after_all(context):
    context.browser.quit()
