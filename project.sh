function project() {
  echo "### Running script... Please wait ###"
  cd
  mkdir $1
  project.py $1
  cd ./$1
  git init
  git remote add origin https://github.com/rootGuillaume/$1.git
  touch README.md
  touch .gitignore
  git add .
  git commit -m "first commit"
  git push origin master
  #atom
  echo "### Process complete ###"
}


function webproject() {
  echo "### Running script... Please wait ###"

  cd
  mkdir $1
  project.py $1
  cd ./$1

  git init
  git remote add origin https://github.com/rootGuillaume/$1.git

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
  #atom

  echo "### Process complete ###"
}
