#Aqui são feitos os metodos para acessar o SQLAlchemy
from ..models import tarefa_model
from api import db

def cadastrar_tarefa(tarefa):
    tarefa_db = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao,
                                    data_expiracao=tarefa.data_expiracao)
    db.session.add(tarefa_db)
    db.session.commit()
    return tarefa_db

def listar_tarefas():
    tarefas = tarefa_model.Tarefa.query.all()
    return tarefas

def listar_tarefa_id(id):
    tarefa = tarefa_model.Tarefa.query.filter_by(id=id).first()
    return tarefa