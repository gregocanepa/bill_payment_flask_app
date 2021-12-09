from flask import Flask
from bill_payment.extensions import db
from .commands import create_tables
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
app.cli.add_command(create_tables)
migrate = Migrate(app, db)
CORS(app)

from bill_payment.payables import routes, models
from bill_payment.transactions import models, routes
