from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

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
            # Validation réussie, vous pouvez ajouter ici la logique pour stocker l'utilisateur, par exemple, dans une base de données
            return HTTPFound(location=request.route_url('new_home'))  # Mettez à jour 'home' ici
        else:
            # Validation échouée, vous pouvez renvoyer un message d'erreur à afficher dans le formulaire
            return {'error_message': 'Les mots de passe ne correspondent pas'}

    return {}

