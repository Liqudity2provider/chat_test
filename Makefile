install:
	pip install -r requirements/prod.txt
	pip install -e .

clean:
	isort src

	brunette src

	isort setup.py
	brunette setup.py

lint:
	flake8 --show-source src
	isort --check-only src --diff

	flake8 --show-source setup.py
	isort --check-only setup.py --diff

check:
	brunette src --check
	brunette setup.py --check
