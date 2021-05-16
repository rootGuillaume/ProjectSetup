import sys
from tools.github import GitHub


action = sys.argv[1]
name = sys.argv[2]

print(action, name)

# Create new repository
if action.lower() == "create":
    GitHub.create_repo(name)

# Delete existing repository
if action.lower() == "delete":
    GitHub.delete_repo(name)
