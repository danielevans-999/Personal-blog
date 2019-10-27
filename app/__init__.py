from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db =SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    
    app = Flask(__name__)
    
      
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    
    db.init_app(app)
    bootstrap.init_app(app)
    
    return app
    