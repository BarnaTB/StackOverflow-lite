from flask import Flask
from api.routes import mod

app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix=('/api/v1'))
