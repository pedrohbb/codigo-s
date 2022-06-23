from src.entities.cliente import Cliente
from src.business.cadastro_cliente import CadastroCliente

clt1 = Cliente('1','clt1','rua1','1111-1111')
cadast = CadastroCliente()
cadast.inserir(clt1)
print(cadast.cadastro)
cadast.resetar_cadastro()
print(cadast.cadastro)
#del cadast.cadastro
#print(cadast.cadastro)
