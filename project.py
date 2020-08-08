import os
import sys
from selenium import webdriver


def new_project():
    project = str(sys.argv[1])
    os.mkdir(project)
    browser = webdriver.Firefox()
    browser.get('https://github.com/login')
    login_input = browser.find_element_by_id('login_field')
    login_input.send_keys("login")
    password_input = browser.find_element_by_id('password')
    password_input.send_keys("password")
    login_submit = browser.find_element_by_name('commit')
    login_submit.submit()


if __name__ == '__main__':
    new_project()
