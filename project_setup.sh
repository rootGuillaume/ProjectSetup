function new_project() {
  #python3 project_setup.py $1
  cd /home/guillaume/Projects/$1
  git init
  git remote add origin git@github.com:user/$1.git
}