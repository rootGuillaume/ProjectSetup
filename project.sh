function project() {
  echo "### Running script... Please wait ###"

  if [ -d $1 ];then
    echo "ERROR: Directory already exists."
    echo "Script stop running."

  # Creating project folder and github repository
  else
    cd
    mkdir $1
    project.py $1
    cd ./$1

    git init
    git remote add origin https://github.com/username/$1.git

    touch README.md
    touch .gitignore

    git add .
    git commit -m "first commit"
    git push origin master

    echo "### Process complete ###"
  fi
}



function webproject() {
  echo "### Running script... Please wait ###"

  if [ -d $1 ];then
    echo "ERROR: Directory already exists."
    echo "Script stop running."

  # Creating project folder and github repository
  else
    cd
    mkdir $1
    project.py $1
    cd ./$1

    git init
    git remote add origin https://github.com/username/$1.git

    mkdir {css,fonts,img,js}

    touch README.md
    touch .gitignore
    touch index.html
    touch css/styles.css
    touch fonts/.keep
    touch img/.keep
    touch js/script.js

    git add .
    git commit -m "first commit"
    git push origin master

    echo "### Process complete ###"
  fi
}



function djangoproject () {
  echo "### Running script... Please wait ###"

  if [ -d $1 ]; then
    echo "ERROR: Directory already exists."
    echo "Script stop running."

  else
    cd
    mkdir $1
    project.py $1
    cd ./$1

    git init
    git remote add origin https://github.com/username/$1.git

    touch README.md
    touch .gitignore
    touch requirements.txt
    echo "venv/" >> .gitignore
    echo "# Python libraries to install via pip" >> requirements.txt

    python3 -m venv venv
    source venv/bin/activate

    echo "Installing Django..."
    pip install Django
    django-admin startproject $1
    echo "Django installed."

    git add .
    git commit -m "first commit"
    git push origin master

    echo "### Process complete ###"
  fi
}
