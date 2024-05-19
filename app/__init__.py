from flask import Flask
from .routes import bp_main
from .models import db
import os

def create_app():
    # Criar uma instância do objeto Flask
    app = Flask(__name__)

    # Gere uma chave secreta aleatória
    secret_key = os.urandom(24)

    # Configurações do banco de dados
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clientes.db'  # Corrigido para usar o formato correto da URL do SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar a extensão SQLAlchemy
    db.init_app(app)

    # Registrar blueprint
    app.register_blueprint(bp_main, url_prefix='/main')

    return app