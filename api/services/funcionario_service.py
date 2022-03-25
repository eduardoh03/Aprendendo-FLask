#Aqui são feitos os metodos para acessar o SQLAlchemy
from ..models import funcionario_model
from api import db
#POST
def cadastrar_funcionario(funcionario):
    funcionario_db = funcionario_model.Funcionario(nome=funcionario.nome, idade=funcionario.idade)
    db.session.add(funcionario_db)
    db.session.commit()
    return funcionario_db
#GET ALL
def listar_funcionarios():
    funcionarios = funcionario_model.Funcionario.query.all()
    return funcionarios
#GET BY ID
def listar_funcionario_id(id):
    funcionario = funcionario_model.Funcionario.query.filter_by(id=id).first()
    return funcionario
#PUT
def editar_funcionario(funcionario_db, funcionario_novo):
    funcionario_db.nome = funcionario_novo.nome
    funcionario_db.idade = funcionario_novo.idade
    db.session.commit()
#DELETE
def remover_funcionario(funcionario):
    db.session.delete(funcionario)
    db.session.commit()