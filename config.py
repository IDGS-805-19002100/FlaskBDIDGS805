import os

class Config(object):
    # La SECRET_KEY es fundamental para que Flask-WTF y los mensajes Flash funcionen [cite: 4, 9]
    SECRET_KEY = "ClaveSecretaExamePizzas"
    SESSION_COOKIE_SECURE = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    # Hemos cambiado el nombre de la base de datos a 'pizzeria_examen'
    # Asegúrate de que el usuario 'root' y la contraseña '1234' coincidan con tu instancia local
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@127.0.0.1/pizzeria_examen'
    SQLALCHEMY_TRACK_MODIFICATIONS = False