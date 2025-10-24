# Переменные
PYTHON = /bin/python
PIP = /bin/pip
SOURCE_DIR = src
TESTS_DIR = tests
REQUIREMENTS = requirements.txt

# Цели по умолчанию
.DEFAULT_GOAL := help

# Помощь по командам
help:
	@echo "Доступные команды:"
	@echo "  install    - Установка зависимостей"
	@echo "  run        - Запуск основного скрипта"
	@echo "  test       - Запуск тестов"
	@echo "  lint       - Проверка кода с flake8"
	@echo "  format     - Форматирование кода black"
	@echo "  clean      - Очистка временных файлов"
	@echo "  req        - Обновление requirements.txt"

# Установка зависимостей
install:
	$(PIP) install -r $(REQUIREMENTS)

# Запуск основной программы
run:
	$(PYTHON) $(SOURCE_DIR)/main.py


.PHONY: help install run test lint format clean req