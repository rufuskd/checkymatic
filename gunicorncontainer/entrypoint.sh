#!/usr/bin/env ash

cd /usr/local/connectorApp
pip install -r requirements.txt
/usr/bin/gunicorn -b 0.0.0.0:8000 -w 4 connectorApp:app
