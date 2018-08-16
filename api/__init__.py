from flask import Flask
<<<<<<< HEAD

app = Flask(__name__)
=======
from api.routes import mod
from api import routes

app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix='/api/v1')
>>>>>>> ft-add-question
