import os
import chromedriver_binary
from selenium import webdriver


# Step 1 -- Create Directories & Files
def createDirectory():
    projects_dir = "C:\\Users\\gasmi\\PlanetGit\\ProjectSetup\\"
    new_project_dir = input("Pick a directory's name :")
    dir_to_create = projects_dir + new_project_dir

    try:
        os.mkdir(new_project_dir, 0o755)
        print("Directory '%s' created succesfully" %new_project_dir)
        print(os.getcwd())

    except OSerror as error:
        print("Failed to create directory")


def createFile(*files_name):
    for file in files_name:
        open(file, "w")


# Step 2 -- Github browser

# WebDriver for Mozilla
# https://github.com/mozilla/geckodriver/releases

def githubActions():
    driver = webdriver.Firefox()
    driver.get("https://github.com/login")

    login_button = driver.find_elements_by_xpath('//*[@id="login_field"]')[0]
    login_button.send_keys("")

    password_button = driver.find_elements_by_xpath('//*[@id="password"]')[0]
    password_button.send_keys("")

    sumbit_button = driver.find_elements_by_xpath('//*[@id="login"]/form/div[4]/input[9]')[0]
    submit_button.click()

#createDirectory()
#createFile(".gitignore", "README.md")
githubActions()







#os.chdir(new_project_dir)

#print(os.getcwd())
