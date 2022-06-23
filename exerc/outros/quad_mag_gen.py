#determinando escopo do problema
def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]

        remLst = lst[:i] + lst[i+1:]

        for p in permutation(remLst):
            l.append([m] + p)
    return l

n = int(input('insira um inteiro: '))

perm_set = permutation([k for k in range(1,(n**2)+1)])

matricesn_n = list()
for perm in perm_set:
    matricesn_n.append([perm[k*n:(k+1)*n] for k in range(n)])


#criando conjunto solução - um subconjunto do escopo
solutions = list()
for matrix in matricesn_n:
    aux = sum(matrix[0])
    print(aux)

    #impondo condição sob as linhas
    linesum = set([sum(matrix[i]) for i in range(n)])
    linesum.add(aux)

    if len(linesum) != 1:                    
        continue
    
    #impondo condição sob as colunas
    columnsum = set([sum([matrix[i][j] for i in range(n)]) for j in range(n)])
    columnsum.add(aux)

    if len(columnsum) != 1:                 
        continue
    
    #impondo condição sob as diagonais
    diagonalsum = set([sum([matrix[i][i] for i in range(n)]), sum([matrix[n-1-j][j] for j in range(n)])])   
    diagonalsum.add(aux)

    if len(diagonalsum) != 1:
        continue
    
    solutions.append(matrix)

print(len(solutions)) 

                

                    

