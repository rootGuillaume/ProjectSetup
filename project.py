#!/usr/bin/python3
import os
import sys
from selenium import webdriver

def new_project():
    project = str(sys.argv[1])

    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')

    browser = webdriver.Firefox(options=options)
    browser.get('https://github.com/login')

    print("Attempt to connect to github...")
    login_input = browser.find_element_by_id('login_field')
    login_input.send_keys("login")
    password_input = browser.find_element_by_id('password')
    password_input.send_keys("password")
    login_submit = browser.find_element_by_name('commit')
    login_submit.submit()
    print("Succesfully connected.")

    while browser.current_url != "https://github.com/":
        continue
    else:
        browser.get('https://github.com/new')

    repo_name = browser.find_element_by_id('repository_name')
    repo_name.send_keys(project)
    repo_submit = browser.find_element_by_id('new_repository')
    repo_submit.submit()
    print("Creating repository...")

    while browser.current_url != "https://github.com/username/" + project:
        continue
    else:
        browser.close()
        print("Succesfully created.")


if __name__ == '__main__':
    new_project()
