# Application de Chat avec Pyramid

![Logo de l'Application](projet/image.png)

> Cette application de chat basique a été développée avec le framework Pyramid et le langage de programmation Python. Elle permet aux utilisateurs de s'inscrire, de se connecter, et de participer à un chat en temps réel. Les messages sont stockés dans un fichier JSON pour la persistance des données.


## 🚀 Fonctionnalités Principales

- **Authentification des Utilisateurs :** Les utilisateurs peuvent s'inscrire et se connecter pour accéder au chat.
  
- **Interface Utilisateur Intuitive :** Les pages sont conçues de manière conviviale, avec des fonctionnalités d'inscription, de connexion, de page d'accueil, et de chat.

- **Chat en Temps Réel :** Les utilisateurs authentifiés peuvent envoyer des messages et participer à un chat en temps réel.

- **Gestion des Sessions :** L'application utilise des sessions pour suivre l'état d'authentification des utilisateurs.


## 🛠️ Installation

1. **Cloner le Projet :** `git clone https://github.com/mkonate19/ALPHA.git`
2. **Installer les Dépendances :** `cookiecutter gh:Pylons/pyramid-cookiecutter-starter`



## ⚙️ Configuration

1. **Configurer le Chemin du Fichier JSON des Utilisateurs :** Mettez à jour le chemin du fichier `users.json` dans `views.py`.
   ```python
   USERS_JSON_PATH = 'chemin/vers/le/fichier/users.json'
2. **Configurer le Chemin du Fichier JSON des Messages :** Mettez à jour le chemin du fichier `users.json` dans `views.py`.
   ```python
   MESSAGES_JSON_PATH = 'chemin/vers/le/fichier/messages.json'



## 🚀 Installation

1. **Lancer l'Application : ** `pserve3 developpement.ini`
2. **Accéder à l'Application : Ouvrez un navigateur et allez à :** `http://localhost:6543`



## 🐞 Problèmes rencontrés

1. **Architecture de pyramide**
2. **Inscription : Problèmes liés à l’ajout et au stockage des données des utilisateurs**
3. **Messagerie : Problèmes de stockage des messages et de duplication lors de l'actualisation :**
4. **Interdiction d'envoyer un même message en doublon**
5. **Inversion de l'ordre des messages stockés (du plus récent au plus ancien)**



## 🤝 Contributions

> Les contributions sous forme de suggestions, rapports de bogues, ou pull requests sont les bienvenues. N'hésitez pas à ouvrir une issue pour discuter de nouvelles fonctionnalités ou de modifications importantes.



## 📝 Licence

> Ce projet est sous licence [MIT](LICENSE)

