# Variables
SHELL := /bin/bash
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
DOCKER_IMAGE = health-calculator
PORT = 5001


# Commandes disponibles
help:
	@echo "Available commands:"
	@echo "  make init       - Create a virtual environment and install dependencies"
	@echo "  make run        - Run the Flask app locally"
	@echo "  make build      - Build the Docker image"
	@echo "  make test       - Run the unit tests"
	@echo "  make run-container - Build and run the containerized application"
	@echo "  make stop       - Stop the running container"
	@echo "  make clean      - Remove stopped containers"

# Initialisation de l'environnement virtuel
init:
	@echo "Initialization..."
	@echo "Création d'un environnement virtuel" ; \
	python3 -m venv .venv ; \
	source .venv/bin/activate && \
	echo "Installation des librairies" && \
	pip install -r requirements.txt

# Lancer l'application Flask localement
run:
	$(PYTHON) app.py

# Construire l'image Docker
build:
	docker build -t $(DOCKER_IMAGE) .

# Lancer les tests unitaires
test:
	$(PYTHON) -m unittest discover -s . -p "*.py"

# Lancer des tests API
test-api:
	$(PYTHON) test_api.py

# Lancer l'application Dockerisée
run-container:
	@echo "Lancement du conteneur Docker..."
	docker run -p $(PORT):$(PORT) --name health-calculator-container $(DOCKER_IMAGE)

# Arrêter les conteneurs
stop:
	docker stop $$(docker ps -q --filter ancestor=$(DOCKER_IMAGE))

# Nettoyer les conteneurs arrêtés
clean:
	docker rm -f $$(docker ps -aq --filter ancestor=$(DOCKER_IMAGE))

# Lancer toutes les étapes du projet en une seule commande
all: init test build run-container
	@echo "Tout est prêt ! L'application est lancée dans le conteneur Docker."
