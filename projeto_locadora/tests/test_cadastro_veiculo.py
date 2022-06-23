from src.business.cadastro_veiculo import CadastroVeiculo
from src.entities.veiculo import Veiculo
from src.exceptions.veiculo_not_found_error import VeiculoNotFoundError
import pytest


@pytest.fixture
def setup():
    CadastroVeiculo.resetar_cadastro()

def test_inserir(): 
    aux = CadastroVeiculo()
    lst = []
    for i in range(1,5):
        lst.append(Veiculo(...))
        
    for veiculo in lst:
        aux.inserir(veiculo)

    assert lst == aux.cadastro

@pytest.mark.parametrize('test_input,expected', [('1',Veiculo(...)),
                        ('2',Veiculo(...))])
def test_consultar(test_input,expected,setup):
    aux0 = CadastroVeiculo()
    aux1 = Veiculo(...)
    aux2 = Veiculo(...)
    aux0.inserir(aux1)
    aux0.inserir(aux2)

    assert aux0.consultar(test_input).__dict__ == expected.__dict__

def test_remover_por_id(setup):
    aux0 = CadastroVeiculo()
    aux1 = Veiculo(...) 
    aux0.inserir(aux1)
    aux3 = aux0.cadastro[:]
    aux0.remover_por_id(...)

    assert aux0.cadastro == [] and aux3 == [aux1]

def test_remover_por_entidade(setup):
    aux0 = CadastroVeiculo()
    aux1 = Veiculo(...)
    aux0.inserir(aux1)
    aux3 = aux0.cadastro[:]
    aux0.remover_por_entidade(aux1)

    assert aux0.cadastro == [] and aux3 == [aux1]