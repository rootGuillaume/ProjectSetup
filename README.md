# GitHub Project Setup


## Installation :inbox_tray:

You need to install [Selenium](https://selenium-python.readthedocs.io/) before running "SCRIPT".

```bash
pip install selenium
```

Then install Firefox webdriver to run the browser. Open your terminal and run following commands.

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
login_input.send_keys("username") # Line 12

password_input.send_keys("password") # Line 14

while browser.current_url != "https://github.com/username/" + project: # Line 28
```

Then, update your GitHub account's url in **project.sh** with GitHub username.

```bash
$ git remote add origin https://github.com/repo/$1.git # Line 8
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

Settings done we finally can create our github project. Open your terminal and run custom bash function.

```bash
$ project name_of_your_project
```
