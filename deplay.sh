git pull
source env/bin/activate
pip install -r requirements.txt
python server/manage.py migrate
python server/manage.py collectstatic --noinput
sudo supervisorctl restart gunicornMsMaps
sudo service nginx restart