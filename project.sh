function project() {
  echo "### Running script... Please wait ###"
  cd
  mkdir $1
  python3 /home/guillaume/Projects/ProjectSetup/project.py $1
  cd ./$1
  git init
  touch .gitignore
  touch README.md
  git add .
  git commit -m "first commit"
  git push -u origin master
  echo "### Process complete ###"
}
