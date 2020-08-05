import os
import sys
import chromedriver_binary
from selenium import webdriver

new_project = input("Pick a directory's name :")

# Step 1 -- Create Directories & Files
def createDirectory():
    projects_dir = "C:\\Users\\gasmi\\PlanetGit\\ProjectSetup\\"
    dir_to_create = projects_dir + new_project

    try:
        os.mkdir(new_project, 0o755)
        print("Directory '%s' created succesfully" %new_project)
        print(os.getcwd())

    except OSerror as error:
        print("Failed to create directory")


def createFile(*files_name):
    for file in files_name:
        open(file, "w")

# Step 2 -- Github browser
driver = webdriver.Chrome()

def githubLogin():
    driver.get("https://github.com/login")
    login_button = driver.find_element_by_id("login_field")
    login_button.send_keys("")
    password_button = driver.find_element_by_id("password")
    password_button.send_keys("")
    submit_button = driver.find_element_by_name("commit").click()


def githubRepository():
    driver.get("https://github.com/new")
    repo_name_field = driver.find_element_by_id("repository_name")
    repo_name_field.send_keys(new_project)
    create_repo = driver.find_element_by_id("new_repository").submit()

def githubAddRemote():
    remote_cmd_line = driver.find_element_by_id("empty-setup-push-repo-echo").text
    print(remote_cmd_line)

#createDirectory()
#createFile(".gitignore", "README.md")

githubLogin()
githubRepository()
githubAddRemote()
