import sys
from tools.github import GitHub


action = sys.argv[1]
#name = sys.argv[2]

GitHub.list_repo()

if action.lower() == "list":
    GitHub.list_repo()

"""
# Create new repository
if action.lower() == "create":
    GitHub.create_repo(name)

# Delete existing repository
if action.lower() == "delete":
    GitHub.delete_repo(name)
"""
