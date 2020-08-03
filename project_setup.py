import os

def CreateDirectory():
    projects_dir = "C:\\Users\\gasmi\\PlanetGit\\ProjectSetup\\"
    new_project_dir = input("Pick a directory's name :")
    dir_to_create = projects_dir + new_project_dir

    try:
        os.mkdir(new_project_dir, 0o755)
        print("Directory '%s' created succesfully" %new_project_dir)
        print(os.getcwd())

    except OSerror as error:
        print("Failed to create directory")

CreateDirectory()
