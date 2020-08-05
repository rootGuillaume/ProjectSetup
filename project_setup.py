import os
import chromedriver_binary
from selenium import webdriver

# Execute functions and command lines
def createDirectory():
    try:
        os.mkdir(new_project, 0o755)
        print("Directory '%s' created succesfully" %new_project)
        os.system('git init')
    except FileExistsError:
        print("!!! '%s' already exist !!!" %new_project)
        new_project = input("Please, choose an other project name :")

def createFile(*files_name):
    #open(os.path.join(dir_to_create), files_name)
    for file in files_name:
        open(file, "w")
        print(files_name, "created succesfully")

def githubLogin():
    driver.get("https://github.com/login")
    login_button = driver.find_element_by_id("login_field")
    login_button.send_keys("") # Login
    password_button = driver.find_element_by_id("password")
    password_button.send_keys("") # Password
    submit_button = driver.find_element_by_name("commit").click()

def githubRepository():
    driver.get("https://github.com/new")
    repo_name_field = driver.find_element_by_id("repository_name")
    repo_name_field.send_keys(new_project)
    create_repo = driver.find_element_by_id("new_repository").submit()

def githubAddRemote():
    remote_cmd_line = driver.find_elements_by_xpath('//*[@id="empty-setup-push-repo-echo"]/span[1]')[0].text
    os.system(remote_cmd_line)


# Execute functions and command lines
new_project = input("Project name :")
print("### Project setup processing... Please wait ###")

projects_dir = "C:\\Users\\gasmi\\PlanetGit\\ProjectSetup\\"
dir_to_create = projects_dir + new_project

createDirectory()

driver = webdriver.Chrome()

githubLogin()
githubRepository()
githubAddRemote()
createFile(".gitignore", "README.md")

os.system('git add .')
os.system('git commit -m "initial commit"')
os.system('git push origin master')

print("### Process complete ###")
