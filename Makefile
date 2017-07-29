.PHONY: dev build

dev:
	flask run --host 0.0.0.0 --port $(PORT) --reload --no-debugger

build:
	pip install -e .