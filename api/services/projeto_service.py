#Aqui são feitos os metodos para acessar o SQLAlchemy
from ..models import projeto_model
from api import db
#POST
def cadastrar_projeto(projeto):
    projeto_db = projeto_model.Projeto(nome=projeto.nome, descricao=projeto.descricao)
    db.session.add(projeto_db)
    db.session.commit()
    return projeto_db
#GET ALL
def listar_projetos():
    projetos = projeto_model.Projeto.query.all()
    return projetos
#GET BY ID
def listar_projeto_id(id):
    projeto = projeto_model.Projeto.query.filter_by(id=id).first()
    return projeto
#PUT
def editar_projeto(projeto_db, projeto_novo):
    projeto_db.nome = projeto_novo.nome
    projeto_db.descricao = projeto_novo.descricao
    db.session.commit()
#DELETE
def remover_projeto(projeto):
    db.session.delete(projeto)
    db.session.commit()