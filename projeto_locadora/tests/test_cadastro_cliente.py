from src.business.cadastro_cliente import CadastroCliente
from src.entities.cliente import Cliente
from src.exceptions.cliente_not_found_error import ClienteNotFoundError
import pytest


@pytest.fixture
def setup():
    CadastroCliente.resetar_cadastro()

def test_inserir(): 
    aux = CadastroCliente()
    lst = []
    for i in range(1,5):
        lst.append(Cliente(f'{i}', f'clt{i}', f'rua{i}', f'{i}'*8))
        
    for cliente in lst:
        aux.inserir(cliente)

    assert lst == aux.cadastro

@pytest.mark.parametrize('test_input,expected', [('1',Cliente('1', 'clt1', 'rua1', '1'*8)),
                        ('2',Cliente('2', 'clt2', 'rua2', '2'*8))])
def test_consultar(test_input,expected,setup):
    aux0 = CadastroCliente()
    aux1 = Cliente('1', 'clt1', 'rua1', '1'*8)
    aux2 = Cliente('2', 'clt2', 'rua2', '2'*8)
    aux0.inserir(aux1)
    aux0.inserir(aux2)

    assert aux0.consultar(test_input).__dict__ == expected.__dict__

def test_remover_por_id(setup):
    aux0 = CadastroCliente()
    aux1 = Cliente('1', 'clt1', 'rua1', '1'*8) 
    aux0.inserir(aux1)
    aux3 = aux0.cadastro[:]
    aux0.remover_por_id('1')

    assert aux0.cadastro == [] and aux3 == [aux1]

def test_remover_por_entidade(setup):
    aux0 = CadastroCliente()
    aux1 = Cliente('1', 'clt1', 'rua1', '1'*8)
    aux0.inserir(aux1)
    aux3 = aux0.cadastro[:]
    aux0.remover_por_entidade(aux1)

    assert aux0.cadastro == [] and aux3 == [aux1]