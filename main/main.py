import sys, os
from tools.github import GitHub
from tools.env import Env
from secrets import GIT_DIR

#os.chdir(GIT_DIR)
#Env.linux_env("test")
#print(Env.get_os())

#action = sys.argv[1]
#name = sys.argv[2]
#private = sys.argv[3]
#
#GitHub.create_repo(name, True)


for count, arg in enumerate(sys.argv):




#for count, arg in enumerate(sys.argv):

#
#    # Create a new repository
#    if count == 1 and arg.lower() == 'create':
#        if count == 2:
#            name = arg
#
#            # Check if private
#            if count == 3 and arg.lower() == 'private':
#                GitHub.create_repo(name, True)
#
#            else:
#                GitHub.create_repo(name, False)
#
#        else:
#            sys.exit()




#action, name = "", ""

"""
for count, arg in enumerate(sys.argv):
    print(count, arg)

    if sys.argv[count] == 1:
        action = sys.argv[count]
        print(action)

    elif sys.argv[count] == 2:
        name = sys.argv[count]
        print(name)

if action.lower() == "list":
    GitHub.list_repo()

# Create new repository
elif action.lower() == "create":
    GitHub.create_repo(name)

# Delete existing repository
if action.lower() == "delete":
    GitHub.delete_repo(name)
"""
