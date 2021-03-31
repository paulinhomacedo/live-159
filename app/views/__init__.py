from .home import blueprint as home

blueprints = {home,}

def init_app(app):    
    for bp in blueprints:
        app.register_blueprint(bp)
