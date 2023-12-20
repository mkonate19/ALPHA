def includeme(config):
    config.add_route('new_home', '/')
    config.add_route('register', '/register')
    config.add_route('home', '/home')  # Ajoutez cette ligne pour la route 'home'
    config.add_route('login', '/login')  # Ajout de la route pour la page de connexion
    config.add_route('chat', '/chat')  # Ajout de la route pour la vue du chat



