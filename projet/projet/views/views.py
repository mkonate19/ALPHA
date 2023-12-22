import json
import os
import datetime
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

# Définissez le chemin du fichier users.json dans le répertoire 'views'
USERS_JSON_PATH = 'users.json'  # Mettez à jour le chemin du fichier
MESSAGES_JSON_PATH = 'messages.json'  # Ajoutez le chemin du fichier pour les messages

# Définir le chemin du fichier de journal
LOG_FILE_PATH = 'app_log.txt'  # Mettez à jour le chemin du fichier


def read_users():
    try:
        with open(USERS_JSON_PATH, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    return users

def write_users(users):
    with open(USERS_JSON_PATH, 'w') as f:
        json.dump(users, f)

def read_messages():
    """
    Lit les messages à partir d'un fichier JSON.

    Returns:
        list: Une liste de messages, chaque message étant un dictionnaire.

    Raises:
        IOError: En cas d'erreur lors de la lecture du fichier.

    Note:
        Cette fonction lit les messages à partir du fichier spécifié par la variable globale
        `MESSAGES_JSON_PATH`. Si le fichier n'existe pas, il sera créé avec une liste vide de messages.

    Exemple:
        messages = read_messages()
    """
    if not os.path.exists(MESSAGES_JSON_PATH):
        # Créer le fichier messages.json s'il n'existe pas
        write_messages([])

    try:
        with open(MESSAGES_JSON_PATH, 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = []
    return messages

def write_messages(messages):
    # Sauvegarder la liste mise à jour dans le fichier JSON
    try:
        with open(MESSAGES_JSON_PATH, 'r') as f:
            existing_messages = json.load(f)
    except FileNotFoundError:
        existing_messages = []

    # Ajouter uniquement les nouveaux messages à la liste existante
    existing_messages.extend(message for message in messages if message not in existing_messages)

    # Sauvegarder la liste mise à jour dans le fichier JSON
    try:
        with open(MESSAGES_JSON_PATH, 'w') as f:
            json.dump(messages, f)
        print("Écriture dans le fichier JSON réussie.")
    except Exception as e:
        print(f"Erreur lors de l'écriture dans le fichier JSON : {e}")

def write_to_log(message):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'{timestamp} - {message}\n'

    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(log_entry)
        print("Écriture dans le fichier de journal réussie.")

@view_config(route_name='new_home', renderer='templates/new_home.jinja2')
def new_home_view(request):
    # Vérifiez si l'utilisateur est connecté
    if 'user_authenticated' in request.session:
        # L'utilisateur est connecté, récupérez son adresse e-mail
        user_email = request.session.get('user_email')

        # Exemple d'utilisation de la fonction de journalisation
        write_to_log(f'Page d\'accueil visitée par {user_email}')

        welcome_message = f"Bienvenue sur notre page d'accueil, {user_email}!"
    else:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return HTTPFound(location=request.route_url('login'))

    # Ajoutez des données spécifiques à la nouvelle page ici
    data = {
        'title': 'Nouvelle Page d\'Accueil',
        'content': welcome_message,
    }
    return data

@view_config(route_name='register', renderer='templates/register.jinja2')
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Charger les utilisateurs depuis le fichier JSON
        users = read_users()

        # Ajoutez ici la logique pour valider le formulaire
        # Par exemple, vérifiez si le mot de passe et la confirmation sont identiques
        if password == confirm_password:
            # Vérifier si l'utilisateur existe déjà
            if email in users:
                return {'error_message': 'L\'utilisateur existe déjà'}

            # Ajouter l'utilisateur à la liste
            users[email] = {'password': password}

            # Sauvegarder la liste mise à jour dans le fichier JSON
            write_users(users)

            # Exemple d'utilisation de la fonction de journalisation
            write_to_log(f'Nouvel utilisateur enregistré : {email}')


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
        users = read_users()

        # Vérifier si l'utilisateur existe et si le mot de passe correspond
        if email in users and users[email]['password'] == password:
            # L'utilisateur est authentifié, stockez une indication d'authentification dans la session
            request.session['user_authenticated'] = True
            request.session['user_email'] = email  # Stockez d'autres informations d'utilisateur si nécessaire

            write_to_log(f'Utilisateur connecté : {email}')

            # Rediriger vers la page d'accueil
            return HTTPFound(location=request.route_url('new_home'))

        # L'authentification a échoué, renvoyer un message d'erreur à afficher dans le formulaire
        return {'error_message': 'L\'authentification a échoué'}

    return {}

@view_config(route_name='logout')
def logout_view(request):
    # Récupérez l'utilisateur déconnecté
    user_email = request.session.get('user_email')

    # Exemple d'utilisation de la fonction de journalisation
    write_to_log(f'Utilisateur déconnecté : {user_email}')

    # Supprimez les informations d'authentification de la session
    request.session.pop('user_authenticated', None)
    request.session.pop('user_email', None)

    # Redirigez l'utilisateur vers la page de connexion après la déconnexion
    return HTTPFound(location=request.route_url('login'))




def append_message_to_json(user, message):
    # Charger les messages depuis le fichier JSON
    messages = read_messages()

    # Ajouter le nouveau message avec des informations temporelles
    new_message = {'user': user, 'message': message}
    messages.append(new_message)

    # Sauvegarder la liste mise à jour dans le fichier JSON
    write_messages(messages)


from pyramid.httpexceptions import HTTPSeeOther

@view_config(route_name='chat', renderer='templates/chat.jinja2')
def chat_view(request):
    # Vérifiez si l'utilisateur est connecté
    if 'user_authenticated' not in request.session:
        # L'utilisateur n'est pas connecté, redirigez-le vers la page de connexion
        return HTTPFound(location=request.route_url('login'))

    # Récupérez l'utilisateur connecté
    user_email = request.session.get('user_email')

    if request.method == 'POST':
        # L'utilisateur est connecté, récupérez son adresse e-mail
        user = user_email
        message = request.POST.get('message')

        # Ajouter le message au fichier JSON
        append_message_to_json(user, message)
        
        # Exemple d'utilisation de la fonction de journalisation
        write_to_log(f'Nouveau message de {user} : {message}')

        # Rediriger vers la même page après le traitement POST
        return HTTPSeeOther(request.route_url('chat'))

    # Charger les utilisateurs depuis le fichier JSON
    users = read_users()

    # Charger les messages depuis le fichier JSON
    messages = read_messages()

    return {'users': users, 'messages': messages, 'user_email': user_email}



