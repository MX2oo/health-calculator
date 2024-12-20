# Health Calculator Microservice

## Description
Ce projet consiste en un microservice Flask permettant de calculer deux métriques de santé importantes :
- **BMI (Body Mass Index)** : Indice de masse corporelle.
- **BMR (Basal Metabolic Rate)** : Taux métabolique de base.

L'application est containerisée avec Docker, automatisée avec Makefile, testée via des tests unitaires, et déployée automatiquement sur **Azure App Service** à l'aide de GitHub Actions.

---

## Fonctionnalités
1. **Endpoints disponibles** :
   - `/bmi` : Calcul du BMI.
   - `/bmr` : Calcul du BMR.

2. **Calculs** :
   - **BMI** : `weight (kg) / (height (m))²`
   - **BMR** (Formule Harris-Benedict) :
     - Homme : `88.362 + (13.397 x poids (kg)) + (4.799 x taille (cm)) - (5.677 x âge)`
     - Femme : `447.593 + (9.247 x poids (kg)) + (3.098 x taille (cm)) - (4.330 x âge)`

---

## Prérequis
- **Python 3.11 ou supérieur**
- **Docker**
- **Azure App Service**

---

## Installation

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/MX2oo/health-calculator
   cd health-calculator
   ```

2. **Installer les dépendances** :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Lancer l'application localement** :
   ```bash
   python app.py
   ```
   L'application sera accessible sur `http://127.0.0.1:5000`.

---

## Usage

### Tester les endpoints
- **BMI** :
  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"height": 1.75, "weight": 70}' \
  http://127.0.0.1:5000/bmi
  ```

- **BMR** :
  ```bash
  curl -X POST -H "Content-Type: application/json" \
  -d '{"height": 175, "weight": 70, "age": 25, "gender": "male"}' \
  http://127.0.0.1:5000/bmr
  ```

---

## Utilisation avec Docker

1. **Construire l'image Docker** :
   ```bash
   docker build -t health-calculator:latest .
   ```

2. **Lancer un conteneur Docker** :
   ```bash
   docker run -d -p 5001:5001 health-calculator:latest
   ```

3. **Accéder à l'application** :
   - URL : `http://127.0.0.1:5001`.

---

## Automatisation avec Makefile

### Commandes disponibles
- **Installation des dépendances** :
  ```bash
  make init
  ```
- **Exécution de l'application** :
  ```bash
  make run
  ```
- **Lancer les tests** :
  ```bash
  make test
  ```
- **Construire l'image Docker** :
  ```bash
  make build
  ```

---

## Tests

Des tests unitaires ont été écrits pour valider les fonctionnalités suivantes :
1. Calculs des métriques BMI et BMR.
2. Fonctionnement des endpoints `/bmi` et `/bmr`.

### Lancer les tests
```bash
python -m unittest discover -s . -p "*.py"
```

---

## Déploiement CI/CD avec GitHub Actions

Un pipeline CI/CD est configuré dans le fichier `.github/workflows/ci-cd.yml` pour :
1. Exécuter les tests unitaires.
2. Construire l'image Docker.
3. Déployer automatiquement sur **Azure App Service**.

### Configuration pour Azure
1. Télécharger le **Publish Profile** depuis Azure.
2. Ajouter le fichier dans les **Secrets GitHub** sous le nom `AZURE_WEBAPP_PUBLISH_PROFILE`.

### Déploiement automatique
- Chaque push sur la branche `main` déclenche le pipeline CI/CD.

---

## Structure du Projet
```plaintext
.
├── app.py                # API Flask avec les endpoints
├── health_utils.py       # Fonctions utilitaires pour les calculs
├── requirements.txt      # Dépendances Python
├── Dockerfile            # Containerisation
├── Makefile              # Automatisation
├── test.py               # Tests unitaires
├── .github/workflows/ci-cd.yml # Pipeline CI/CD
└── README.md             # Documentation du projet
```

---