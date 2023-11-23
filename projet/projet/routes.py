def includeme(config):
    config.add_route('new_home', '/')
    config.add_route('register', '/register')
    config.add_route('home', '/home')  # Ajoutez cette ligne pour la route 'home'
