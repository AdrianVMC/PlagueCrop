run:
	@python3 main.py

dev:
	@watchmedo auto-restart --patterns="*.py" --recursive -- python3 main.py

clean:
	@find . -type d -name "__pycache__" -exec rm -r {} +
	@find . -type f -name "*.pyc" -delete
	@find . -type f -name "*.pyo" -delete
