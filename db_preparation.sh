#!/usr/bin/env bash

# скрипт для применения миграции и заполнения базы данных

python ./tools/csv_to_json.py
python ./manage.py migrate
python ./manage.py loadall
