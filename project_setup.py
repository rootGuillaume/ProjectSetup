import os
import chromedriver_binary
from selenium import webdriver

# ======================= Functions =======================
def createDirectory(dir):
    try:
        os.mkdir(dir, 0o755)
        print("Directory '%s' created succesfully" %dir)
        os.system('git init')
    except FileExistsError:
        print("!!! '%s' already exist !!!" %dir)
        new_project = input("Please, choose an other project name :")

def createFile():
    open(os.path.join(path, "README.md"), "w")
    open(os.path.join(path, ".gitignore"), "w")

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


# ======================= Main =======================
new_project = input("Project name :")
print("### Project setup processing... Please wait ###")

projects_dir = "C:\\Users\\gasmi\\PlanetGit\\ProjectSetup\\"
dir_to_create = projects_dir + new_project

cwd = os.getcwd()
path = cwd + "\\" + new_project

createDirectory(new_project)

driver = webdriver.Chrome()

githubLogin()
githubRepository()
githubAddRemote()
createFile()


os.chdir(path)

if os.getcwd() == path:
    os.system('git add .')
    os.system('git commit -m "initial commit"')
    os.system('git push origin master')
else:
    print("ERROR PATH")
    print(path)
    print(os.getcwd())

#os.system('git add .')
#os.system('git commit -m "initial commit"')
#os.system('git push origin master')

print("### Process complete ###")
