# """
# How Bootcamps - Stone - /código[s]
# Data: 24/03/2022
# Autor: Henrique Junqueira Branco
# Enunciado: BINGO do zero!

# Uma cartela de BINGO consiste em 5 colunas de 5 números que são rotulados com as letras B, I, N, G e O.
# Atenção: Google it, para quem nunca viu uma cartela dessas!

# Existem 15 números que podem aparecer sob cada letra respeitando a regra abaixo.
# - B -> números variando de 1 a 15  (inclusos)
# - I -> números variando de 16 a 30 (inclusos)
# - N -> números variando de 31 a 45 (inclusos)
# - ... e assim por diante

# Passo número 0:
# - Escreva uma função que crie uma cartela de BINGO aleatória. Dica(podemos usar um dicionário!). 
# - As chaves serão as letras B, I, N, G e O. 
# - Os valores serão as listas de cinco números aleatórios respeitando a regra dos intervalos de cada letra. 

# Passo número 1: 
# - Escreva uma segunda função que exiba a cartela de BINGO com as colunas rotuladas apropriadamente
# - Formate a saída no terminal para que a cartela seja impressa em forma de colunas (letras e seus valores abaixo)

# Passo número 2: 
# - Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.

# Passo número 3:
# - Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
# - Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.

# Passo número desafio:
# - Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
#     * O número mínimo de sorteio para que a carteja seja vencedora (não necessariamente preencher toda a cartela!)
#     * A média do número de sorteios para que a carteja seja vencedora
#     * O número máximo de sorteios para que a cartela seja vencedora
# """
import random
from copy import deepcopy

letras = 'BINGO'
numb = [i for i in range(1,76)]
numb_select = []
qtd = []

def card():
    card_ = dict()
    for i in range(0,5):
        card_[letras[i]] = []
        interv_numbers = [(15*i+j) for j in range(1,16)]
        count = 1
        while count <= 5:
            rand_numb = random.choice(interv_numbers)
            (card_[letras[i]]).append(rand_numb)
            interv_numbers.remove(rand_numb)
            count += 1
    return card_

def format_card(card):
    matrix = list(card.items())
    card_format = []
    line = []
    for i in range(0,5):
        line.append(matrix[i][0])
    card_format.append(line)

    for j in range(0,5):
        line = []
        for i in range(0,5):
            line.append(matrix[i][1][j])
        card_format.append(line)

    return card_format

def sort_and_check(cards):

    #sort
    x = random.choice(numb)
    numb_select.append(x)    #essa linha e a seguinte não é boa prática, mas n vi outra forma simples
    numb.remove(x)

    #check
    if (x % 15) != 0:
        column = (x // 15)
    else:
        column = (x // 15) - 1

    for i in range(len(cards)):        
        Checked = False
        for j in range(1,6):
            if cards[i][j][column] == x:
                Checked = True
                break
        if Checked:
            (cards[i])[j][column] = 'XX'
    return cards
    
def rounds(cards):
    count = 1
    winners = []
    while (count <= 75) and (len(winners) < 1):         
        cards = sort_and_check(cards) 

        #round announce
        if len(numb_select) % 6 != 0: 
            print(f'TURNO {len(numb_select)}-', end='')
            for i in range(0,5):
                if numb_select[-1] // 15 == i:                
                    print(f'sorteio: {letras[i]}, {numb_select[-1]} |', end=' ')
                    break
            if numb_select[-1] == 75:
                print(f'sorteio: O, {numb_select[-1]} |', end=' ')
        else:
            print(f'\n\nTURNO {len(numb_select)}-', end='')
            for i in range(0,5):
                if numb_select[-1] // 15 == i:                
                    print(f'sorteio: {letras[i]}, {numb_select[-1]} |', end=' ')
                    break
            if numb_select[-1] == 75:
                print(f'sorteio: O, {numb_select[-1]} |', end=' ')


        #winner check
        round_winner = []
        for player_card in cards:   #line condition
            winner = False
            for m in range(1,6):
                for n in range(0,5):
                    blank_line = False 
                    if player_card[m][n] != 'XX':
                        break
                    else:
                        blank_line = True
                if blank_line:
                    winner = True
                    break
            if winner:
                round_winner.append(cards.index(player_card))           

        for player_card in cards:   #column condition   
            winner = False
            for m in range(0,5):
                for n in range(1,6):
                    blank_column = False 
                    if player_card[n][m] != 'XX':
                        break
                    else:
                        blank_column = True
                if blank_column:
                    winner = True
                    break
            if winner:
                round_winner.append(cards.index(player_card))
                
        #winner find
        if len(round_winner) > 0:
            winners.append(round_winner)

        count += 1

    return winners, cards

def players():
    plyrs = []
    while True:
        try:
            a = int(input("Extract a new random card_? 1 ---> Yes / 0 ---> No : "))
            if a in {0,1}:
                if bool(a):
                    card_ = card()
                    plyrs.append(format_card(card_))
                    print("Random card printed!")
                else:
                    print('\n')
                    break
            else:
                print("Invalid format! Try again")
                continue
        except:
            print("Invalid format! Try again")
            continue

    if plyrs == []:
        quit()
    else:
        return plyrs

def announce(plyrs, winners, endcards):
    global numb, numb_select, qtd

    q = len(numb_select) // 15
    r = len(numb_select) % 15

    print(f'\n\n{len(numb_select)} numbers randomly selected:')

    for j in range(q):
        for k in range(15):
            print(numb_select[15*j + k], end=' ')
        print(' ')
    
    if r > 0:
        for l in numb_select[-r:]:
            print(l, end=' ')

    print('\n')

    for i in range(len(winners[0])):
        print(f"\t\t\t   >>>> THE PLAYER {winners[0][i]+1} WON THE PRIZE! <<<<\n")
        for m in range(0,6):
            for n in range(0,5):
                print(f'{plyrs[winners[0][i]][m][n]}', end='\t')
            print('----->\t\t', end='')
            for n in range(0,5):
                print(f'{endcards[winners[0][i]][m][n]}', end='\t')
            print('\n')

    qtd.append(len(numb_select))      
    numb = [i for i in range(1,76)]
    numb_select = []

def main():
    players_bingo = players()
    mutab_cards = deepcopy(players_bingo)
    winners, mutab_cards = rounds(mutab_cards)
    announce(players_bingo, winners, mutab_cards)


main()


