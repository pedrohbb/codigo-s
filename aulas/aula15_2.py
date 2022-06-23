from aula15 import Funcionario

funcionario1 = Funcionario('João','da Silva', 3000)

funcionario2 = Funcionario('Antonio','Pereira', 2500)

funcionario3 = Funcionario('Sérgio','Ramos', 4000)


#print(funcionario1.__salario_inicial)
#funcionario1.__salario_inicial =  10000
#print(funcionario1.__salario_inicial)
funcionario1.salario()

funcionario1.dar_aumento(0.1)

funcionario1.salario()

#print(funcionario1.__salario_atual)