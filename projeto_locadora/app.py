from src.entities.cliente import Cliente
from src.entities.entidade import Entidade
from src.entities.pessoa_fisica import PessoaFisica
from src.entities.pessoa_juridica import PessoaJuridica
from src.business.cadastro_cliente import CadastroCliente
from flask import Flask, request

app = Flask(__name__)

cadastro_cliente = CadastroCliente()

@app.route("/cliente", methods=["POST"])
def inserir_cliente():
    dados = request.json
    #cliente = PessoaFisica(dados)
    #cadastro_cliente.inserir()
    return 'teste', 201
    
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/stone", methods=['POST'])
# def stone():
#     return "stone codigo[s]"

# @app.route("/cliente", methods=['PUT'])
# def atualizar_cliente():
#     return "stone codigo[s]"

# @app.route("/veiculo", methods=["DELETE"])
# def deletar_veiculo():
#     return "stone codigo[s]"