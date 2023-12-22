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
    """
    Lire les utilisateurs depuis le fichier JSON.

    Returns:
        dict: Un dictionnaire représentant les utilisateurs. Si le fichier
              n'existe pas, renvoie un dictionnaire vide.
    """
    try:
        with open(USERS_JSON_PATH, 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}
    return users

def write_users(users):
    """
    Écrit les données des utilisateurs dans un fichier JSON.

    Args:
        users (dict): Un dictionnaire représentant les informations des utilisateurs.

    Exemple:
        write_users({'user1': {'password': 'pass1'}, 'user2': {'password': 'pass2'}})
    """
    with open(USERS_JSON_PATH, 'w') as f:
        json.dump(users, f)

def read_messages():
    """
    Lit les messages à partir d'un fichier JSON.

    Returns:
        list: Une liste de messages, chaque message étant un dictionnaire.

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
    """
    Écrire les messages dans le fichier JSON, en fusionnant avec les messages existants.

    Cette fonction prend une liste de nouveaux messages en paramètre, les fusionne avec les messages
    existants lus à partir du fichier JSON, puis sauvegarde la liste mise à jour dans le même fichier.

    Args:
        messages (list): Une liste de nouveaux messages à ajouter.

    Example:
        write_messages([{'user': 'john@example.com', 'message': 'Hello!'}])
    """
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
    """
    Écrire un message dans le fichier de journal.

    Cette fonction prend en paramètre un message, ajoute un horodatage au format '%Y-%m-%d %H:%M:%S',
    puis enregistre le message dans le fichier de journal spécifié par la variable LOG_FILE_PATH.

    Args:
        message (str): Le message à enregistrer dans le journal.

    Affiche:
        str: Un message indiquant le succès de l'écriture dans le fichier de journal.

    Exemple:
        write_to_log("Ceci est un message de journal.")
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'{timestamp} - {message}\n'

    with open(LOG_FILE_PATH, 'a') as log_file:
        log_file.write(log_entry)
        print("Écriture dans le fichier de journal réussie.")

@view_config(route_name='new_home', renderer='templates/new_home.jinja2')
def new_home_view(request):
    """
    Affiche la vue de la nouvelle page d'accueil.

    Cette fonction vérifie si l'utilisateur est connecté en inspectant la session de la requête.
    Si l'utilisateur est connecté, elle récupère l'adresse e-mail de l'utilisateur et enregistre
    une entrée de journal indiquant la visite de la page d'accueil par cet utilisateur.
    Ensuite, elle génère un message de bienvenue personnalisé. Si l'utilisateur n'est pas connecté,
    la fonction redirige l'utilisateur vers la page de connexion.

    Args:
        request (pyramid.request.Request): L'objet de requête Pyramid.

    Returns:
        dict: Un dictionnaire contenant les données à rendre dans le modèle.
              Le dictionnaire contient les clés 'title' et 'content', où 'title' est défini comme
              'Nouvelle Page d'Accueil' et 'content' est le message de bienvenue ou une redirection HTTPFound.
    """
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
    """
    Vue pour l'enregistrement d'un nouvel utilisateur.

    Args:
        request (pyramid.request.Request): L'objet de requête Pyramid.

    Returns:
        dict or HTTPFound: Si la méthode de la requête est POST et la validation du formulaire est réussie,
        renvoie un objet dict contenant les données à rendre dans le modèle.
        Sinon, renvoie un objet dict contenant un message d'erreur à afficher dans le formulaire
        ou un objet HTTPFound pour rediriger vers une autre page.
    """
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
    """
    Vue pour la connexion de l'utilisateur.

    Cette vue gère les demandes POST provenant du formulaire de connexion.
    Elle récupère l'adresse e-mail et le mot de passe à partir des données
    du formulaire, vérifie l'authenticité des informations en les comparant
    avec celles stockées dans le fichier JSON des utilisateurs, puis
    effectue les actions appropriées en conséquence.

    Args:
        request (pyramid.request.Request): L'objet de demande Pyramid.

    Returns:
        dict or HTTPFound: Si la connexion réussit, la vue renvoie un
        objet HTTPFound pour rediriger l'utilisateur vers la page d'accueil.
        En cas d'échec, elle renvoie un dictionnaire contenant un message
        d'erreur à afficher dans le formulaire de connexion.

    """
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
    """
    Vue pour la déconnexion de l'utilisateur.

    Args:
        request (pyramid.request.Request): L'objet de requête associé à la vue.

    Returns:
        pyramid.httpexceptions.HTTPFound: Redirection vers la page de connexion.
    """
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
    """
    Ajoute un nouveau message au fichier JSON des messages.

    Charge la liste actuelle de messages depuis le fichier JSON, ajoute un nouveau message
    avec des informations temporelles, puis sauvegarde la liste mise à jour dans le fichier JSON.

    Args:
        user (str): L'adresse e-mail de l'utilisateur qui envoie le message.
        message (str): Le contenu du message à ajouter.

    Example:
        append_message_to_json('john@example.com', 'Salut, comment ça va?')
    """
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
    """
    Cette vue gère l'affichage de la page de chat, ainsi que l'ajout de nouveaux messages
    lorsque l'utilisateur soumet un formulaire. Si l'utilisateur n'est pas connecté, il est
    redirigé vers la page de connexion.

    Args:
        request (pyramid.request.Request): L'objet de requête Pyramid.

    Returns:
        dict or HTTPSeeOther: Si la requête est de type POST, la fonction ajoute un nouveau
        message et redirige l'utilisateur vers la même page avec HTTPSeeOther. Sinon, elle renvoie
        un dictionnaire contenant les utilisateurs, les messages et l'e-mail de l'utilisateur
        connecté pour l'affichage dans le modèle.
    """
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



