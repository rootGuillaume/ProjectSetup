import os
from selenium import webdriver

class Webdriver:

    # Firefox headless webdriver
    def firefox():
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        browser = webdriver.Firefox(options=options)
        return browser
