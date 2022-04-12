"""Bootcamp Dev Python - codigo[s] Stone - HowBootcamps

Grupo 41

desenvolvedores: Pedro Henrique Birindiba Batista
                 Miguel Zaqueu Lourenço Araújo"""

import random
import copy
import os
import time
from IPython.display import clear_output

def mazegenerator(m,n):
    """
    Considera dois inteiros 'm' e 'n' e retorna uma lista 'labirinto' com  'm' linhas, 'n' colunas e entrada-saída ao longo da dimensão de
    maior comprimento. A construção do labirinto é feita concatenando-se linhas. Ela é dividida em etapas: a linha 0 é criada; em seguida 
    as linhas 1 até m-2 e por fim a última linha. Por razões de compensação, considera-se a mudança de variáveis nas primeiras linhas 
    desse código (para mais detalhes, ver comentário da função trapfinder).
    """
    
                                                          
    transp_axis = (m < n)                 
    if transp_axis:                                
        m, n = n, m                                      
                                                 
    
    maze = [list('##' for _ in range(n))]         #linha 0 (bordo do labirinto)    

    line = []                 #constrói linha 1
    while len(line) == 0:

        for i in range(n):

            if (i == 0) or (i == n-1):
                line.append('##')                                        
            else:
                clear = random.choice((0, 1))

                if clear:
                    line.append('  ')
                else:
                    line.append('##')

    maze.append(line)

    for _ in range(2, m-1):                 #constrói linhas restantes (exceto a linha da saída)                        
       
        connected = False
        while not connected:
            line = []

            for j in range(n):
                if (j == 0) or (j == n-1):
                    line.append('##')
                else:   
                    clear = random.choice((0, 1))

                    if clear:
                        line.append('SS')
                    else:
                        line.append('##')
                
            maze.append(line)

            if not trapfinder(maze):
                connected = True

            if connected:

                for j in range(1,n-1):

                    if maze[-1][j] == 'SS':
                        maze[-1][j] = '  '
                
            else:
                del maze[-1]
            

    #geração da última linha e saída: a função tracker garante a passagem de uma linha anterior para a seguinte, mas não se pode
    #prever por quais colunas pode chegar. por isso a última linha recebe tratamento separado.
    #ao replicar este trecho do código com pequenas alterações pode-se gerar saídas em diferentes eixos.

    wayout = m-1, random.randint(1,n-2)
    connected = False
    count = 1
    while not connected:
        maze.append(['##' for _ in range(n)])                   #última linha
        maze[wayout[0]][wayout[1]] = 'SS'

        if not trapfinder(maze):
            connected = True
        
        elif count <= n**2:
            count += 1
            del maze[-1]
            wayout = m-1, random.randint(1,n-2)
            continue

        else:

            while trapfinder(maze):
                maze[m-2][random.randint(1,n-2)] = '  '
            
            connected = True

    #gera a entrada --- condição imposta na linha 0
    while True:
        entrance = posicionar_aleatorio(maze, '  ', ['SS', '  '])
        if entrance[0] == 0 and maze[1][entrance[1]] == '  ':
            break
        else:
            maze[entrance[0]][entrance[1]] = '##'
    
            

    #desfaz a mudança de variável
    if transp_axis:
        m, n = n, m
        transp_maze = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                transp_maze[i][j] = maze[j][i]  
        maze = transp_maze
        
        # toma a coordenada transposta da posição inicial 
        entrance = entrance[1], entrance[0]

    return maze, entrance


def printmaze(maze):
    m = len(maze)
    n = len(maze[0])

    for i in range(m):
        for j in range(n):
            print(maze[i][j], end='')
        print('')


def posicionar_aleatorio(labirinto:list, caracter_a_posicionar:str, lista_a_ignorar:list or None = None) -> tuple:

    '''Posiciona um caracter em uma posição válida

    labirinto: lista de listas
    x: índice que marca início do conjunto de posições a ser consideradoy: última linha da lista
    caracter_a_posicionar: qual caracter deve ser posicionado
    lista_a_ignorar: lista de caracteres os quais caracter_a_posicionar não pode ocupar a posição
    retorna: uma tupla linha, coluna da posição em que o robo foi inserido

    '''
    m = len(labirinto)
    n = len(labirinto[0])
    
    linha = random.randint(0, m-1)
    coluna = random.randint(0, n-1)

    if labirinto[linha][coluna] in lista_a_ignorar:
        return posicionar_aleatorio(labirinto, caracter_a_posicionar, lista_a_ignorar)

    labirinto[linha][coluna] = caracter_a_posicionar

    return linha, coluna


def movimento_aleatorio(labirinto: list, posicao_atual: tuple, procurado: str) -> tuple or bool:
    '''Verifica se o robo pode ser movimentar para uma posição procurada
    
    retorna False se o robo NÃO pode se movimentar para uma posição procurada,
    ou a posição se o robo pode se movimenta para uma posição procurada'''
   
    linha = posicao_atual[0]
    coluna = posicao_atual[1]
    lista_direcoes = ['direita', 'esquerda', 'baixo', 'cima']

    
    for _ in range(4):
        direcao_escolhida = random.choice(lista_direcoes)
        lista_direcoes.remove(direcao_escolhida)
        
        try:
            #movimenta para direita
            if (direcao_escolhida == 'direita') and (labirinto[linha][coluna+1] == procurado):
                return linha, coluna+1

            #para esquerda
            if (direcao_escolhida == 'esquerda') and labirinto[linha][coluna-1] == procurado:
                return linha, coluna-1

            #para baixo
            if (direcao_escolhida == 'baixo') and labirinto[linha+1][coluna] == procurado:
                return linha+1, coluna

            #para cima
            if (direcao_escolhida == 'cima') and labirinto[linha-1][coluna] == procurado:
                return linha-1, coluna
        except:
            pass

    return False

def tracker(maze, current_posit, stack, state=False):
    """maze: lista labirinto
    current_posit: posição atual do robô
    stack: pilha de posições já visitadas
    state: parâmetro para imprimir
    notas: persegue iteradamente uma saída """


    if state:
        printmaze(maze)
        time.sleep(0.3)
        os.system('cls' if os.name == 'nt' else 'clear')
        #clear_output(wait=True)
    
    #movimenta para a saída
    if movimento_aleatorio(maze, current_posit, 'SS'):
        return 'way out'
    
    #movimenta para '  '
    next_posit = movimento_aleatorio(maze, current_posit, '  ')

    if next_posit:
        #salva posição atual na pilha
        stack.append(current_posit)

        #coloca '--' na posição atual
        maze[current_posit[0]][current_posit[1]] = '--'

        #muda a posição do robô
        current_posit = next_posit
        maze[current_posit[0]][current_posit[1]] = 'RT'

        return tracker(maze, current_posit, stack, state)

    #se não há caminho novo, marca a posição sem passagem, não a adiciona na pilha e retorna
    else:
        maze[current_posit[0]][current_posit[1]] = '--'
        
        try:
            current_posit = stack.pop()
            maze[current_posit[0]][current_posit[1]] = 'RT'

            return tracker(maze, current_posit, stack, state)
       
        except:

            return 'trap'

def trapfinder(maze):
    """ (ver comentário função tracker) modificação da função tracker para construir iteradamente uma lista labirinto concatenando-se colunas. """
    
    n = len(maze[0])            
    for j in range(1,n-1):
        mazetest = copy.deepcopy(maze)
        if (mazetest[-2][j] == '  ') and (mazetest[-1][j] == '##'):
            stack = []
            mazetest[-2][j] = 'RT'

            if tracker(mazetest, (-2,j), stack) == 'trap':
                return True                                                
        else:
            continue
    
    return False

def main():
    m = 10
    n = 20
    maze, initial_posit = mazegenerator(m,n)
    stack = []
    tracker(maze, initial_posit, stack, True)

main()