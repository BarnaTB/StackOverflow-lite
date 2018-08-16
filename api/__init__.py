from flask import Flask
<<<<<<< HEAD
<<<<<<< HEAD

app = Flask(__name__)
=======
from api.routes import mod
from api import routes

app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix='/api/v1')
>>>>>>> ft-add-question
=======
from routes import mod

app = Flask(__name__)

app.register_blueprint(routes.mod, url_prefix='/api/v1/questions')
app.register_blueprint(routes.mod, url_prefix='/api/v1')
>>>>>>> ft-add-answer
