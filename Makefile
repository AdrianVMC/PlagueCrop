run:
	python3 main.py

install:
	pip install -r requirements.txt

test:
	pytest tests/

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -r {} +

lint:
	flake8 .

help:
	@echo "Comandos disponibles:"
	@echo "  make run       -> Ejecuta la simulación"
	@echo "  make install   -> Instala dependencias"
	@echo "  make test      -> Ejecuta los tests"
	@echo "  make clean     -> Limpia archivos .pyc y __pycache__"
	@echo "  make lint      -> Linting con flake8"
