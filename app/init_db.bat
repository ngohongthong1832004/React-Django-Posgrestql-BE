@echo off
del /F db.sqlite3
del main\migrations\0001_initial.py

call python manage.py makemigrations

call python manage.py migrate

call python init_db.py

rmdir /s /q main\migrations\__pycache__
rmdir /s /q main\__pycache__
rmdir /s /q Vis4T_main\__pycache__


call python manage.py createsuperuser