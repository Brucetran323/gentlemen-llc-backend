
from flask import Flask
# from .payments.routes import payments 

from config import Config

from .auth.routes import auth
# from .services.routes import services
# from .api.routes import api
# from .mass_text.routes import mass_text

from .models import db, User, customerContact
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
from flask_cors import CORS


app = Flask(__name__)
# CORS(app)

# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


login = LoginManager()
moment = Moment(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.loginPage'



app.register_blueprint(auth)
# app.register_blueprint(services)
# app.register_blueprint(api)
# app.register_blueprint(mass_text)
# app.register_blueprint(payments)

from . import routes 

