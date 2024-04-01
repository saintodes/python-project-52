install:
	poetry install

tests:
	poetry run python3 manage.py test .

run:
	poetry run python3 manage.py runserver

shell:
	python manage.py shell_plus --print-sql

makemigrations:
	poetry run python3 manage.py makemigrations

migrate:
	poetry run python3 manage.py migrate

makemessages-ru:
	poetry run django-admin makemessages -l ru


compile-messages:
	poetry run django-admin compilemessages

lint:
# 	poetry run flake8 task_manager/ --count --select=E9,F63,F7,F82 --show-source --statistic
	poetry run flake8 task_manager/ --show-source --statistics --max-line-length=100 --exclude=task_manager/*/migrations/*



.PHONY: build

build:
	@./build.sh

cov:
	poetry run python -m coverage run manage.py test
	poetry run coverage xml -o coverage.xml

