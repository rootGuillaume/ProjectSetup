# GitHub Project Setup

## Installation :inbox_tray:

You need to install [Selenium](https://selenium-python.readthedocs.io/) before running "SCRIPT".

```bash
pip install selenium
```

Now feel free to download the repository.

```bash
$ cd
$ cd Downloads/
$ git clone https://github.com/rootGuillaume/ProjectSetup.git
```

Then you need to install Firefox webdriver to run the browser. Open your terminal and run following commands.

```bash
$ wget https://github.com/mozilla/geckodriver/releases/tag/v0.27.0-linux64.tar.gz
$ tar -xvzf geckodriver-v0.27.0-linux64.tar.gz
$ chmod +x geckodriver
$ sudo mv geckodriver /usr/local/bin
```


## Configuration :wrench:

First, you need to update **project.py** with your GitHub username and password.

```python
login_input.send_keys("username") # Line 14

password_input.send_keys("password") # Line 16
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
