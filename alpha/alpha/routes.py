# routes.py
def includeme(config):
    config.add_route('register', '/register', request_method='GET')
    config.add_route('register_post', '/register', request_method='POST')
    config.add_route('home', '/home')
    config.scan('.views')

