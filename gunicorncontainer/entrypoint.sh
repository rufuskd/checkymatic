#!/usr/bin/env ash

cd /usr/local/connectorApp
pip3 install -r requirements.txt
/usr/bin/gunicorn --log-file /var/log/gunerr.log --access-logfile /var/log/gunacc.log -b 0.0.0.0:8000 -w 4 connectorApp:app
