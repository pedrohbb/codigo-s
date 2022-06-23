from aula16 import Funcionario

funcionario1 = Funcionario('João','da Silva', 3000)

funcionario2 = Funcionario('Antonio','Pereira', 2500)

funcionario3 = Funcionario('Sérgio','Ramos', 4000)

#Em Python não existem atributos privados. Não há maneira canônica de fazê-lo.
#Existe uma solução parcial para este problema, além da ética de trabalho, que é
#através do uso de duplo underscore presente no script de criação da classe no atributo desejado
#Ele faz com que este atributo receba o prefixo '_classname' em scripts que o importe. Por exemplo,
print(funcionario1.__salario_inicial)
#gera um tempo em erro de execução do tipo AttributeError, pois o mesmo não existe mas
print(funcionario1._Funcionario__salario_inicial)
#printa o valor do atributo original. Dessa forma, não se tem acesso a variável da forma usual e todo
#e qualquer tipo de invocação se faz via prefixo


