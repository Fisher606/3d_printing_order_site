from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'main.login'  # Указываем правильный маршрут для входа в систему

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
