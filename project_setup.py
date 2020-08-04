import os
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

# WebDriver for Mozilla
# https://github.com/mozilla/geckodriver/releases
driver = webdriver.Firefox()

def githubLogin():
    driver.get("https://github.com/login")

    login_button = driver.find_elements_by_xpath('//*[@id="login_field"]')[0]
    login_button.send_keys("")

    password_button = driver.find_elements_by_xpath('//*[@id="password"]')[0]
    password_button.send_keys("")

    submit_button = driver.find_element_by_name("commit")
    submit_button.click()


def githubRepository():
    driver.get("https://github.com/new")
    repo_name_field = driver.find_elements_by_xpath('//*[@id="repository_name"]')[0]
    repo_name_field.send_keys(new_project)

    create_button = driver.find_elements_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')[0]
    create_button.click()


#createDirectory()
#createFile(".gitignore", "README.md")
githubLogin()
githubRepository()
