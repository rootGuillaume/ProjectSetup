new_prject() {
  python project_setup.py $1
  cd /Users/""/Documents/Projects/$1
  git init
  git remote add origin git@github.com:rootGuillaume/$1.git
}
