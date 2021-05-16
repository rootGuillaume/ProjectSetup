#!/usr/bin/python3
import os
import sys
from selenium import webdriver

class GitHub:

    # Function to create a new repository
    def create_repo(name):
        project = name#str(sys.argv[1])

        # Running Firefox headless mode
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')

        browser = webdriver.Firefox(options=options)
        browser.get('https://github.com/login')

        # Logging to github
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

        # Repository creation
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

        return 1


    # Function to delete a new repository
    def create_repo(name):
        return 1
