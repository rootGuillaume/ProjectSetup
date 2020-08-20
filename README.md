# GitHub Project Setup

Creating a GitHub project, .gitignore or README.md file and pushing the first commit is always following the same procedure. In this case why should we keep going ? Let's automate this stuff ! :bulb:

:pushpin: **The project is meant to be use for Linux distributions such as Ubuntu.**


## Installation :inbox_tray:

First, you need to install python [Selenium](https://selenium-python.readthedocs.io/) library.

```bash
$ pip install selenium
```

Then install Firefox [geckodriver](https://github.com/mozilla/geckodriver/releases) to run the browser. Open your terminal and run following commands.

```bash
$ wget https://github.com/mozilla/geckodriver/releases/tag/v0.27.0-linux64.tar.gz

$ tar -xvzf geckodriver-v0.27.0-linux64.tar.gz

$ chmod +x geckodriver

$ sudo mv geckodriver /usr/local/bin
```

Now feel free to download the repository.

```bash
$ cd

$ cd Downloads/

$ git clone https://github.com/rootGuillaume/ProjectSetup.git
```


## Configuration :wrench:

First, you need to update **project.py** with your GitHub username and password.

```python
login_input.send_keys("username") # Line 19

password_input.send_keys("password") # Line 21

while browser.current_url != "https://github.com/username/" + project: # Line 38
```

Then, update your GitHub account's url in **project.sh** with GitHub username.

```bash
$ git remote add origin https://github.com/username/$1.git # Line 16 & 46
```




## Execution :computer:

The project setup use both project.sh bash script and project.py python script.
The python script is running through the bash script.
You have to _source_ the bash script to run **project** function wherever you want.

```bash
$ cd Downloads/ProjectSetup/ # Navigate to the project.sh folder

$ source project.sh
```

Now the most important step is to make the python script runnable anywhere.
We assume we have a **script** folder where to put scripts. If not you can create one wherever you want.
(e.g : Here we use ~/scripts)

```bash
$ cd

$ mkdir scripts

$ mv Downloads/ProjectSetup/project.py ~/scripts

$ cd ~/scripts

$ chmod +x project.py

$ cd /usr/local/bin/

$ sudo ln -s ~/scripts/project.py .

```

Now the python script can be run anywhere you want to.


## Create project :pencil2:

Settings done we finally can create our github project. Open your terminal and run one of both custom bash functions.

```bash
$ project name_of_your_project

$ webproject name_of_your_project
```
##

_V1.1.1 | Last Update : 08/20/20_
