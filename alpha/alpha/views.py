# Fichier: your_project/your_project/views.py

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='register', renderer='alpha:templates/register.jinja2', request_method='GET')
def register_get_view(request):
    return {}

@view_config(route_name='register', renderer='alpha:templates/register.jinja2', request_method='POST')
def register_post_view(request):
    if registration_is_successful(request):
        # Redirige vers la page d'accueil après une inscription réussie
        return HTTPFound(location=request.route_url('home'))
    return {}

def registration_is_successful(request):
    # Implémentez la logique pour vérifier si l'inscription est réussie
    # Par exemple, vous pouvez vérifier les données du formulaire dans request.POST
    # et retourner True si l'inscription est valide, sinon False.
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirmPassword')

    # Implémentez votre logique de vérification ici
    # ...

    # Exemple simple : vérifiez si le mot de passe et la confirmation sont identiques
    return password == confirm_password

@view_config(route_name='home', renderer='alpha:templates/home.jinja2')
def home_view(request):
    return {}
