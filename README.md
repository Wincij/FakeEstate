# FakeEstate

Fake estate agency application build with Django 2.1 framework and PostgreSQL database. 
Fully customized, composed admin page. Landing page contains lastest listings and "Seller of the Month". 
Everyone can make an inquiry, but only registered users are notificated when inquiry is open. Site also has listing search engine.

All requirements are placed in "requirements.txt" file.

RUN (easy way):

1. Create new virtual envirnoment
2. Activate it `source VENV_NAME/bin/activate`
3. Install all requirements `pip install -r requirements.txt`
4. Create a database of any kind (I used Postgres, but as long as it is small app sqlite3 will work fine)
5. Open settings file `btre/btre/settings.py` and set up all parameters (database and SECRET_KEY)
6. Transfer model schema to your new database by: 
- `python3 manage.py makemigrations`
- `python3 manage.py migrate` 
7. Run local server by `python3 manage.py runserver`
