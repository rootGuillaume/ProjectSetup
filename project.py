import os
import sys
import selenium


def new_project():
    project = str(sys.argv[1])
    os.mkdir(project)
    

if __name__ == '__main__':
    new_project()
