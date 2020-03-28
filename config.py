DEBUG_MODE = True
PORT = 8080
API_ENDPOINT = 'http://127.0.0.1/api/v1.0'

SECRET_KEY = 'example'

SQLALCHEMY_TRACK_MODIFICATIONS = True

ENGINE = 'postgresql+psycopg2'
DB_ENDPOINT = 'example'
DB_PORT = '5432'
DB_USERNAME = 'postgres'
DB_PASSWORD = 'example'
DB_DBNAME = 'postgres'

JWT_SECRET_KEY = 'example'

FIREBASE = {}

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'example@gmail.com'
MAIL_PASSWORD = 'example'


def config(app):
    # GENERAL
    app.config['API_ENDPOINT'] = API_ENDPOINT
    app.config['DEBUG'] = DEBUG_MODE
    app.config['PORT'] = PORT
    app.config['SECRET_KEY'] = SECRET_KEY

    # SQLALCHEMY DATABASE
    db_uri = ENGINE + '://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_ENDPOINT + '/' + DB_DBNAME
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    # FLAK-JWT-EXTENDED
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY

    # SMTP
    app.config['MAIL_SERVER'] = MAIL_SERVER
    app.config['MAIL_PORT'] = MAIL_PORT
    app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
    app.config['MAIL_USERNAME'] = MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

    # FIREBASE
    app.config['FIREBASE'] = FIREBASE
