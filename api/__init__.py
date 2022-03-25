from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
#deve ser adicionado depois do SQLAlchemy para fazer a tradução dos dados python <-> JSON
ma = Marshmallow(app)
migrate = Migrate(app,db)

api = Api(app)

from .views import tarefa_views, projeto_views, funcionario_views
from .models import tarefa_model, projeto_model, funcionario_model
