import os
import sys
import time
from selenium import webdriver


def new_project():
    project = str(sys.argv[1])
    browser = webdriver.Firefox()
    browser.get('https://github.com/login')

    login_input = browser.find_element_by_id('login_field')
    login_input.send_keys("")
    password_input = browser.find_element_by_id('password')
    password_input.send_keys("")
    login_submit = browser.find_element_by_name('commit')
    login_submit.submit()

    time.sleep(2)

    browser.get('https://github.com/new')
    repo_name = browser.find_element_by_id('repository_name')
    repo_name.send_keys(project)
    repo_submit = browser.find_element_by_id('new_repository')
    repo_submit.submit()

    project_url = "https://github.com/rootGuillaume/" + project

    print("Pj url : ", project_url)
    print("Browser : ", browser.current_url)

    while browser.current_url != project_url:
        continue
    else:
        browser.close()

if __name__ == '__main__':
    new_project()
