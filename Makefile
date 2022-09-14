PROJECT_NAME := django-redis
PYTHON_VERSION := 3.10.4
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := redis

# Environment setup
.pip:
	pip install --upgrade pip

setup: .pip
	pip uninstall -y typing
	pip install -U setuptools
	pip install -r requirements.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup

collectstatic:
	python manage.py collectstatic --noinput

code-convention:
	flake8
	pycodestyle

run-redis:
	docker start $(PROJECT_NAME)-redis 2>/dev/null || docker run --name $(PROJECT_NAME)-redis -p 6379:6379 -e REDIS_PASSWORD='$(DATABASE_PASS)' -d redis:7.0.4-alpine

containers-up: run-redis

containers-down:
	docker stop $$(docker ps -aq)

containers-reset: containers-down containers-up
