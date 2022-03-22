from api import ma
from ..models import tarefa_model
from marshmallow import fields
#funciona como o Forms do Django
class TarefaSchema(ma.ModelSchema):
    class Meta:
        model = tarefa_model.Tarefa
        fields = ("id", "titulo", "descricao", "data_expiracao")

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)