#!/usr/bin/python3
import os, sys, time, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
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

        # Check if the repository already exists
        repo_exists = requests.get(f"https://github.com/{USERNAME}/{name}")
        if repo_exists.status_code == 200:
            print("repo already exists")
            return sys.exit(0)

        # Repository creation
        else:
            browser = Webdriver.firefox()

            # Connexion to GitHub
            logged = GitHub.login(browser)

            # New repository
            browser.get('https://github.com/new')

            repo_name = browser.find_element_by_id('repository_name')
            repo_name.send_keys(name)

            repo_submit = browser.find_element_by_id('new_repository')
            repo_submit.submit()

            # Wait for the repository to be create
            while browser.current_url != f"https://github.com/{USERNAME}/" + name:
                continue
            else:
                browser.close()
                print("Succesfully created.")
                return 1



    # Function to delete a new repository
    def delete_repo(name):
        repo = f"rootGuillaume/{name}"

        # Check if the repository already exists
        repo_exists = requests.get(f"https://github.com/{USERNAME}/{name}")
        print(repo_exists.status_code)
        if repo_exists.status_code == 200:

            # Connexion to GitHub
            browser = Webdriver.firefox()
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

        # Repository does not exist
        else:
            print("repo does not exist")
            return sys.exit(0)



    # Get public repositories list
    def list_repo():
        repos = requests.get(f"https://github.com/{USERNAME}?tab=repositories")

        # Get all repositories info
        if repos.status_code == 200:

            # Scraping repositories list
            source = requests.get(f"https://github.com/{USERNAME}?tab=repositories")
            soup = BeautifulSoup(source.text, "html.parser")

            repos_list = soup.find(id="user-repositories-list")
            repos_list = repos_list.find_all("li")

            # Get all repositories informations
            for count, li in enumerate(repos_list):
                repo_name = li.find("a").text
                repo_name = repo_name.replace(" ", "")
                repo_name = repo_name.replace("\n", "")
                repo_url = li.find("a")["href"]

                print(f"[{count + 1}] [{repo_name}] [https://github.com/{USERNAME}/{repo_name}]")

            return sys.exit(1)
