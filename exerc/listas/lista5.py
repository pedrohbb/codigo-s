#1-desafio
import random

while True:

    num_rand = random.randrange(1,100)
    num_user = int(input("Forneça um número inteiro entre de 1 a 100: "))

    if (num_user > 100) or (num_user < 1):
        print("Erro: formato inválido de número")
        continue
    else:
        if num_rand < num_user:
            print("O número sorteado é menor")
        elif num_rand > num_user:
            print("O número sorteado é maior")
        else:
            print("Parabéns! Você acertou o número sorteado")
    
        prompt = input("Deseja jogar novamente? (S/N) -  ")

        if prompt == 'N':
            break
        else:
            continue


    

