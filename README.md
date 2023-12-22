# Application de Chat avec Pyramid

![Logo de l'Application](projet/image.png)

> Cette application de chat basique a été développée avec le framework Pyramid et le langage de programmation Python. Elle permet aux utilisateurs de s'inscrire, de se connecter, et de participer à un chat en temps réel. Les messages sont stockés dans un fichier JSON pour la persistance des données.

## 🚀 Fonctionnalités Principales

- **Authentification des Utilisateurs :** Les utilisateurs peuvent s'inscrire et se connecter pour accéder au chat.
  
- **Interface Utilisateur Intuitive :** Les pages sont conçues de manière conviviale, avec des fonctionnalités d'inscription, de connexion, de page d'accueil, et de chat.

- **Chat en Temps Réel :** Les utilisateurs authentifiés peuvent envoyer des messages et participer à un chat en temps réel.

- **Gestion des Sessions :** L'application utilise des sessions pour suivre l'état d'authentification des utilisateurs.

## 🛠️ Installation

1. **Cloner le Projet :** `git clone [lien du dépôt]`
2. **Installer les Dépendances :** `pip install -r requirements.txt`

## ⚙️ Configuration

1. **Configurer le Chemin du Fichier JSON des Utilisateurs :** Mettez à jour le chemin du fichier `users.json` dans `views.py`.
   ```python
   USERS_JSON_PATH = 'chemin/vers/le/fichier/users.json'
2. **Configurer le Chemin du Fichier JSON des Messages :** Mettez à jour le chemin du fichier `users.json` dans `views.py`.
   ```python
   MESSAGES_JSON_PATH = 'chemin/vers/le/fichier/messages.json'

## 🚀 Installation

1. **Lancer l'Application : ** `python run.py`
2. **Accéder à l'Application : Ouvrez un navigateur et allez à :** `http://localhost:6543`

## 🐞 Problèmes Connus


## 🤝 Contributions

> Les contributions sous forme de suggestions, rapports de bogues, ou pull requests sont les bienvenues. N'hésitez pas à ouvrir une issue pour discuter de nouvelles fonctionnalités ou de modifications importantes.

## 📝 Licence

> Ce projet est sous licence MIT.
