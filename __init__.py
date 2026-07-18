from flask import Flask
from flask_login import LoginManager
from config import Config
from app.models import db, load_user

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    login_manager.user_loader(load_user)

    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.clients.routes import clients_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(clients_bp)

    with app.app_context():
        db.create_all()

    return app
