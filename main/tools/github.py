#!/usr/bin/python3
import os, sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .tools import Webdriver
from secrets import *

class GitHub:

    # Connexion à Github
    def login(webdriver):
        browser = webdriver
        browser.get("https://github.com/login")

        # Username
        login_input = browser.find_element_by_id('login_field')
        login_input.send_keys(USERNAME)

        # Password
        password_input = browser.find_element_by_id('password')
        password_input.send_keys(PASSWORD)

        # Connexion
        login_submit = browser.find_element_by_name('commit')
        login_submit.submit()


        # Test Connexion
        url_failed = "https://github.com/session"
        url_passed = "https://github.com/"

        while browser.current_url != url_failed or url_passed:
            if browser.current_url == url_passed: return True
            elif browser.current_url == url_failed:
                browser.close()
                return sys.exit("Impossible de se connecter")


    # Function to create a new repository
    def create_repo(name):
        project = name#str(sys.argv[1])

        browser = Webdriver.firefox()
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
    def delete_repo(name):
        browser = Webdriver.firefox()

        # Connexion to GitHub
        logged = GitHub.login(browser)

        if logged:
            repo = f"rootGuillaume/{name}"
            browser.get("https://github.com/" + repo + "/settings")

            # Confirm repository deletion
            btn_delete = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[10]/ul/li[4]/details/summary")
            btn_delete.click()

            type_delete = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input")
            type_delete.send_keys(repo)

            confirm_delete = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button")
            confirm_delete.submit()

            # Succesfully supressed
            browser.close()
            print("Repo succesfully delete")
            return sys.exit(1)
