install:
	poetry install

tests:
	poetry run python3 manage.py test .

run:
	poetry run python3 manage.py runserver

shell:
	poetry run python3 manage.py shell

makemessages-ru:
	poetry run django-admin makemessages -l ru


compile-messages:
	poetry run django-admin compilemessages

lint:
	poetry run flake8 task_manager/ --count --select=E9,F63,F7,F82 --show-source --statistics
