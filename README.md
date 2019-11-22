It is best to use the python virtualenv tool to build locally:

1-Install virtual env
sudo pip install virtualenv

2-Create environment
sudo virtualenv --python='/usr/bin/python3' venv

3-Run
source venv/bin/activate	

4-Install requirements
pip install -r requirements.txt

5-Run app
DEVELOPMENT=1 python manage.py runserver
