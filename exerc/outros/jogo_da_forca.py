"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!

A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.

Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

from random import choice
from forkart import WORDS, STATUS

def get_secret_word(words):
    """Devolve uma palavra aleatória de uma lista."""
    
    return choice(words)


def print_game_board():
    """Imprime a situação atual do jogo."""
    
    print("\nLetras corretas: ", end='')
    for i in range(len(correct_letters)):
        if i != len(correct_letters)-1:
            print(correct_letters[i], end= ' ')
        else:
            print(correct_letters[i], end= '')

    print('\t\t\t', end='')

    print("Letras erradas: ", end='')
    for i in range(len(missed_letters)):
        if i != len(missed_letters)-1:
            print(missed_letters[i], end= ' ')
        else:
            print(missed_letters[i], end= '')  

    
def read_input_player():
    """Lê uma letra do usuário."""

    while True:
        char = input("Insira uma letra como palpite: ").lower()
        
        if char not in 'abcdefghijklmnopqrstuvwxyz':     
            print('Entrada inválida! Repita o processo')
            continue

        else:     
            if char in correct_letters:
                print('Você já acertou esse palpite! Agora tente outro!')
                continue
            elif char in missed_letters:
                print('Você já errou esse palpite! Agora tente outro!')
                continue
            elif len(char) == 0 or len(char) >= 2:
                print('Entrada inválida! Repita o processo')
                continue
            else:
                break

    return char


def guess_letter(input_char):
    """Verifica se uma letra está na palavra secreta ou não."""

    if input_char in secret_word:
        correct_letters.append(input_char)
    else:
        missed_letters.append(input_char)
    


def game_continue():
    """Função que decide se jogo já encerrou ou não."""
   
    encoded_word = ''
    for letter in secret_word:
    
        if letter in correct_letters:
            encoded_word += letter
        else:
            encoded_word += '_'

    error = len(missed_letters)
    
    if encoded_word == secret_word:
        print(f'\n\n\t >>>>>> Você venceu! A palavra secreta é {secret_word} <<<<<<')
        return False

    elif error <= attempts:
        if len(missed_letters) > 0:
            print(STATUS[error-1])
            print(f'\n{encoded_word}\n')
            return True
        elif len(correct_letters) > 0:
            print(f'\n{encoded_word}\n')
            return True
        else:
            return True

    else:
        print(f"\n\t>>>>>> Você perdeu! A palavra secreta é {secret_word} <<<<<<")
        print(STATUS[error-1])
        return False

def main():
    while game_continue():
        input_char = read_input_player()
        guess_letter(input_char)
        print_game_board()


secret_word = get_secret_word(WORDS).lower() #palavra selecionada aleatoriamente
correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
attempts = 6  # tentativas


main()

    