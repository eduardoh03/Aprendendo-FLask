from flask_restful import Resource
from api import api
from ..schemas import funcionario_schemas
from flask import request, make_response, jsonify
from ..entidades import funcionario
from ..services import funcionario_service
from ..pagination import paginate
from ..models.funcionario_model import Funcionario

# A view está responsável por tratar os dados das requisições

class FuncionarioList(Resource):  # List é adicionado em metodos que não necessitao de parametros GET e POST

    def get(self):
        # funcionarios = funcionario_service.listar_funcionarios()
        # many é necessario porque várias funcionarios vão ser passadas pelo Schema
        fs = funcionario_schemas.FuncionarioSchema(many=True)
        return paginate(Funcionario, fs)

    def post(self):
        fs = funcionario_schemas.FuncionarioSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)
            result = funcionario_service.cadastrar_funcionario(funcionario_novo)
            return make_response(fs.jsonify(result), 201)


class FuncionarioDetail(Resource):  # Detail é adicionado em metodos que necessitao de parametros PUT e DELETE

    def get(self, id):
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("Funcionario nao encontrado."), 404)
        else:
            fs = funcionario_schemas.FuncionarioSchema()
            return make_response(fs.jsonify(funcionario), 200)

    def put(self, id):
        funcionario_db = funcionario_service.listar_funcionario_id(id)
        if funcionario_db is None:
            return make_response(jsonify("Funcionario nao encontrado."), 404)

        fs = funcionario_schemas.FuncionarioSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            idade = request.json["idade"]
            funcionario_novo = funcionario.Funcionario(nome=nome, idade=idade)
            result = funcionario_service.editar_funcionario(funcionario_db, funcionario_novo)
            funcionario_atualizada = funcionario_service.listar_funcionario_id(id)
            return make_response(fs.jsonify(funcionario_atualizada), 200)

    def delete(self, id):
        funcionario = funcionario_service.listar_funcionario_id(id)
        if funcionario is None:
            return make_response(jsonify("Funcionario nao encontrado."), 404)
        funcionario_service.remover_funcionario(funcionario)
        return make_response(jsonify(""), 204)

# CRIADO A ROTA
api.add_resource(FuncionarioList, '/funcionarios')
api.add_resource(FuncionarioDetail, '/funcionario/<int:id>')