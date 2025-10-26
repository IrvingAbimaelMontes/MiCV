from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Inicializar extensiones
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mi_cv_personal_2024')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mi_cv.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensiones con la app
    db.init_app(app)
    
    # Importar modelos
    from app.models.cv_model import CV
    
    # Registrar blueprints
    from app.routes.cv_routes import cv_bp
    app.register_blueprint(cv_bp, url_prefix='/')
    
    return app

# Exponer la variable 'app' para Gunicorn
app = create_app()
