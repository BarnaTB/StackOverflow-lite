from flask import Flask
from api.routes import mod
from api import routes

app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix='/api/v1')
app.register_blueprint(routes.mod, url_prefix='/api/v1/questions')
app.register_blueprint(routes.mod, url_prefix='/api/v1/auth')
