function project() {
  echo "### Running script... Please wait ###"
  cd
  mkdir $1
  python3 ./project.py $1
  cd ./$1
  git init
  git remote add origin https://github.com/rootGuillaume/$1.git
  touch README.md
  touch .gitignore
  git add .
  git commit -m "first commit"
  git push origin master
  atome
  echo "### Process complete ###"
}
