from api import app
from flask_jwt_extended import JWTManager

app.config['JWT_SECRET_KEY'] = 'jwt-secret-kisumuluzo'

jwt = JWTManager(app)

app.run(debug=True)
