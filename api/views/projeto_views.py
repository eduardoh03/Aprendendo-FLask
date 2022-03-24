from flask_restful import Resource
from api import api
from ..schemas import projeto_schemas
from flask import request, make_response, jsonify
from ..entidades import projeto
from ..services import projeto_service


# A view está responsável por tratar os dados das requisições

class ProjetoList(Resource):  # List é adicionado em metodos que não necessitao de parametros GET e POST

    def get(self):
        projetos = projeto_service.listar_projetos()
        # many é necessario porque várias projetos vão ser passadas pelo Schema
        ps = projeto_schemas.ProjetoSchema(many=True)
        return make_response(ps.jsonify(projetos), 200)

    def post(self):
        ps = projeto_schemas.ProjetoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao)
            result = projeto_service.cadastrar_projeto(projeto_novo)
            return make_response(ps.jsonify(result), 201)


class ProjetoDetail(Resource):  # Detail é adicionado em metodos que necessitao de parametros PUT e DELETE

    def get(self, id):
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("Projeto nao encontrado."), 404)
        else:
            ps = projeto_schemas.ProjetoSchema()
            return make_response(ps.jsonify(projeto), 200)

    def put(self, id):
        projeto_db = projeto_service.listar_projeto_id(id)
        if projeto_db is None:
            return make_response(jsonify("Projeto nao encontrado."), 404)

        ps = projeto_schemas.ProjetoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            projeto_novo = projeto.Projeto(nome=nome, descricao=descricao)
            result = projeto_service.editar_projeto(projeto_db, projeto_novo)
            projeto_atualizada = projeto_service.listar_projeto_id(id)
            return make_response(ps.jsonify(projeto_atualizada), 200)

    def delete(self, id):
        projeto = projeto_service.listar_projeto_id(id)
        if projeto is None:
            return make_response(jsonify("Projeto nao encontrado."), 404)
        projeto_service.remover_projeto(projeto)
        return make_response(jsonify(""), 204)

# CRIADO A ROTA
api.add_resource(ProjetoList, '/projetos')
api.add_resource(ProjetoDetail, '/projeto/<int:id>')