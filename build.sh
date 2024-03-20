#!/bin/bash
# Скрипт для сборки проекта: установка зависимостей и выполнение миграций

echo "Установка зависимостей через Poetry..."
poetry install

echo "Выполнение миграций Django..."
poetry run python manage.py migrate
