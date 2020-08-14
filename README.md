# GitHub Project Setup

## Installation

You need to install [Selenium](https://selenium-python.readthedocs.io/) before running "SCRIPT".

```bash
pip install selenium
```

## Configuration

First, you need to update **project.py** with your GitHub username and password.

```python
login_input.send_keys("username") # Line 14

password_input.send_keys("password") # Line 16
```

Then, update your GitHub account's url in **project.sh** with GitHub username.

```bash
$ git remote add origin https://github.com/username/$1.git
```
