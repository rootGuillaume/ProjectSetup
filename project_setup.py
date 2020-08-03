import os

print(os.getcwd())

projects_dir = "/home/guillaume/Projects/ProjectSetup/"
new_project_dir = input("Pick a directory's name :")
dir_to_create = projects_dir + new_project_dir

try:
    os.mkdir(dir_to_create, 0o755)
    print("Directory '%s' created succesfully" %new_project_dir)
    print(os.getcwd())
except OSerror as error:
    print("Failed to create directory")
