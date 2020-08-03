import os
import webbrowser

projects_dir = "C:\\Users\\gasmi\\PlanetGit\\ProjectSetup\\"
new_project_dir = input("Pick a directory's name :")
dir_to_create = projects_dir + new_project_dir


# Step 1 -- Create Directories & Files
def CreateDirectory():
    try:
        os.mkdir(new_project_dir, 0o755)
        print("Directory '%s' created succesfully" %new_project_dir)
        print(os.getcwd())

    except OSerror as error:
        print("Failed to create directory")

def CreateFile(*files_name):
    for file in files_name:
        open(file, "w")

CreateDirectory()
CreateFile(".gitignore", "README.md")


# Step 2 -- Github browser



#os.chdir(new_project_dir)

#print(os.getcwd())
