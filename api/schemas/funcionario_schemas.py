from api import ma
from ..models import funcionario_model
from marshmallow import fields

#funciona como o Forms do Django
class FuncionarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = funcionario_model.Funcionario
        fields = ("id", "nome", "idade")
        # load_instance = True

    nome = fields.String(required=True)
    descricao = fields.String(required=True)