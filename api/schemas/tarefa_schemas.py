from api import ma
from ..models import tarefa_model
from marshmallow import fields

#funciona como o Forms do Django
class TarefaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = tarefa_model.Tarefa
        fields = ("id", "titulo", "descricao", "data_expiracao", "projeto")
        # load_instance = True

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True, error_messages={"required": "Item necessario.",
                                                                "null": "Esse campo nao pode ser nulo.",
                                                                "validator_failed": "Valor invalido."
                                                                })
    projeto = fields.String(required=True)
