import os
import sys
from selenium import webdriver


def new_project():
    project = str(sys.argv[1])
    os.mkdir(project)
    browser = webdriver.Firefox()
    browser.get("https://github.com/login")

if __name__ == '__main__':
    new_project()
