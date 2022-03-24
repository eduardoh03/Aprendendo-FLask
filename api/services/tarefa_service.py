#Aqui são feitos os metodos para acessar o SQLAlchemy
from ..models import tarefa_model
from api import db
#POST
def cadastrar_tarefa(tarefa):
    tarefa_db = tarefa_model.Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao,
                                    data_expiracao=tarefa.data_expiracao, projeto=tarefa.projeto)
    db.session.add(tarefa_db)
    db.session.commit()
    return tarefa_db
#GET ALL
def listar_tarefas():
    tarefas = tarefa_model.Tarefa.query.all()
    return tarefas
#GET BY ID
def listar_tarefa_id(id):
    tarefa = tarefa_model.Tarefa.query.filter_by(id=id).first()
    return tarefa
#PUT
def editar_tarefa(tarefa_db, tarefa_nova):
    tarefa_db.titulo = tarefa_nova.titulo
    tarefa_db.descricao = tarefa_nova.descricao
    tarefa_db.data_expiracao = tarefa_nova.data_expiracao
    tarefa_db.projeto = tarefa_nova.projeto
    db.session.commit()
#DELETE
def remover_tarefa(tarefa):
    db.session.delete(tarefa)
    db.session.commit()