from flask_restful import Resource
from api import api

class TarefaList(Resource):# List é adicionado em metodos que não necessitao de parametros GET e POST
    def get(self):
        return "Olá Mundo"
api.add_resource(TarefaList, '/tarefas')

# class TarefaDetail(Resource):# Detail é adicionado em metodos que necessitao de parametros PUT e DELETE