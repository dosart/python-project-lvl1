install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even
