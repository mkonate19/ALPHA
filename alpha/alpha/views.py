# Fichier: your_project/your_project/views.py

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

@view_config(route_name='register', renderer='alpha:templates/register.jinja2', request_method='GET')
def register_get_view(request):
    return {}

@view_config(route_name='register', renderer='alpha:templates/register.jinja2', request_method='POST')
def register_post_view(request):
    if registration_is_successful():
        # Redirige vers la page d'accueil après une inscription réussie
        return HTTPFound(location=request.route_url('home'))
    return {}

@view_config(route_name='home', renderer='alpha:templates/home.jinja2')
def home_view(request):
    return {}

