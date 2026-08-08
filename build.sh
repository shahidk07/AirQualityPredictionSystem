#!/usr/bin/env bash
# Render build script
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

cd ibm
python manage.py collectstatic --noinput
