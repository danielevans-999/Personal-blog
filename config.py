import os

class Config:
    '''
    General configuration parent class
    '''
    
    QUOTE_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class TestConfig(Config):
    pass



class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:daniel@localhost/danteblog'
    
    DEBUG = True
    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}