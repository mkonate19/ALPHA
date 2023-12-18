from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    my_session_factory = SignedCookieSessionFactory('itsasecret')
    with Configurator(settings=settings, session_factory=my_session_factory) as config:
        config.include('pyramid_jinja2')
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.include('.routes')
        config.add_route('login', '/login')  # Ajout de la route pour la page de connexion
        config.scan()
    return config.make_wsgi_app()
