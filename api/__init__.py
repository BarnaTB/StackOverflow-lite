from flask import Flask
from routes import mod

app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix='/api/v1/questions')
app.register_blueprint(routes.mod, url_prefix='/api/v1')
