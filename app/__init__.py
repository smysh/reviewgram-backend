from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
    uri = os.environ.get("SQLALCHEMY_DATABASE_URI")
    print(uri)
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://",1)
        print(uri)
    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = uri
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI_TEST")
    
    # Import models here for Alembic setup
    from app.models.user import User
    from app.models.review import Review
    from app.models.watchlist import Watchlist
    from app.models.media import Media
    
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from app.routes.media_routes import media_bp
    app.register_blueprint(media_bp)

    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    from app.routes.autorization_routes import autho_bp
    app.register_blueprint(autho_bp)

    jwt = JWTManager(app)

    CORS(app)
    return app