#!/usr/bin/env ash

cd /usr/local/connectorApp
pip install -r requirements.txt
/usr/bin/gunicorn --bind 0.0.0.0:8000 connectorApp:app
