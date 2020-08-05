import os

cwd = os.getcwd()
dir_test = "TestD"
path = cwd + "\\" + dir_test

os.mkdir(dir_test)
open(os.path.join(path, "test.txt"), "w")
