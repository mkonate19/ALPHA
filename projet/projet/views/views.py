import json
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

# Définissez le chemin du fichier users.json dans le répertoire 'views'
USERS_JSON_PATH = 'users.json'  # Mettez à jour le chemin du fichier

@view_config(route_name='new_home', renderer='templates/new_home.jinja2')
def new_home_view(request):
    # Ajoutez des données spécifiques à la nouvelle page ici
    data = {
        'title': 'Nouvelle Page d\'Accueil',
        'content': 'Bienvenue sur notre nouvelle page d\'accueil!'
    }
    return data

@view_config(route_name='register', renderer='templates/register.jinja2')
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Ajoutez ici la logique pour valider le formulaire
        # Par exemple, vérifiez si le mot de passe et la confirmation sont identiques
        if password == confirm_password:
            # Charger les utilisateurs depuis le fichier JSON
            try:
                with open(USERS_JSON_PATH, 'r') as f:
                    users = json.load(f)
            except FileNotFoundError:
                # Si le fichier n'existe pas, initialisez une structure vide
                users = {}

            # Vérifier si l'utilisateur existe déjà
            if email in users:
                return {'error_message': 'L\'utilisateur existe déjà'}

            # Ajouter l'utilisateur à la liste
            users[email] = {'password': password}

            # Sauvegarder la liste mise à jour dans le fichier JSON
            with open(USERS_JSON_PATH, 'w') as f:
                json.dump(users, f)

            # Validation réussie, rediriger vers la page de connexion
            return HTTPFound(location=request.route_url('login'))  # Mettez à jour 'login' ici
        else:
            # Validation échouée, renvoyer un message d'erreur à afficher dans le formulaire
            return {'error_message': 'Les mots de passe ne correspondent pas'}

    return {}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Charger les utilisateurs depuis le fichier JSON
        try:
            with open(USERS_JSON_PATH, 'r') as f:
                users = json.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas, initialisez une structure vide
            users = {}

        # Vérifier si l'utilisateur existe et si le mot de passe correspond
        if email in users and users[email]['password'] == password:
            # L'utilisateur est authentifié, rediriger vers la page d'accueil
            return HTTPFound(location=request.route_url('new_home'))  # Mettez à jour 'new_home' ici
        else:
            # L'authentification a échoué, renvoyer un message d'erreur à afficher dans le formulaire
            return {'error_message': 'L\'authentification a échoué'}

    return {}
