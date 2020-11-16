.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and libraries"
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Start resting"
	pipenv run pytest tests/tests.py

run:
	@echo "Running python app"
	python3 app.py >> results.txt

deploy:
	@echo "Adding and committing"
	git add results.txt
	git commit -m "Lab 2 com"
	git push  
