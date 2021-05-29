import os
from secrets import GIT_DIR

class Env:

    # Get User Os
    def get_os():
        return os.name


    # Set up for linux env
    def linux_env(repo):
        #print(GIT_DIR)
        commands = [f"cd {GIT_DIR}"]#, f"git clone {repo}"]
        os.chdir(GIT_DIR)
        #for command in commands:
        #    os.system(command)

        #return


    # Set up for windows env
    def windows_env():

        return
