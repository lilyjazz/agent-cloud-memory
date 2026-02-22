.PHONY: install format lint type-check clean help

help:
	@echo "Available commands:"
	@echo "  make install      Install dependencies"
	@echo "  make format       Format code with ruff"
	@echo "  make lint         Check code with ruff"
	@echo "  make type-check   Check types with mypy"
	@echo "  make clean        Remove build artifacts and cache"

install:
	pip install -r requirements.txt
	# Install dev tools if not present (assuming user might not have them)
	pip install ruff mypy pytest types-requests types-PyYAML

format:
	ruff format .

lint:
	ruff check .

type-check:
	mypy .

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
