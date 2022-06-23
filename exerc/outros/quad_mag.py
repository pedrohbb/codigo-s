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

perm_set = permutation([1,2,3,4,5,6,7,8,9])

matrices3_3 = list()
for perm in perm_set:
    matrices3_3.append([perm[:3], perm[3:6], perm[6:]])

#criando conjunto solução - um subconjunto do escopo
solutions = list()
for matrix in matrices3_3:
        soma = sum(matrix[0])

        if sum(matrix[0]) != sum(matrix[1]) or sum(matrix[1]) != sum(matrix[2]):   #impondo condição sob as linhas
            continue
        elif ((soma != (matrix[0][0] + matrix[1][0] + matrix[2][0]))   #impondo condição sob as colunas
        or (matrix[0][0] + matrix[1][0] + matrix[2][0] != matrix[0][1] + matrix[1][1] + matrix[2][1]) 
        or (matrix[0][1] + matrix[1][1] + matrix[2][1] != matrix[0][2] + matrix[1][2] + matrix[2][2])):   
            continue
        elif ((soma != matrix[0][0] + matrix[1][1] + matrix[2][2])   #impondo condição sob as diagonais 
        or (matrix[0][0] + matrix[1][1] + matrix[2][2] != matrix[0][2] + matrix[1][1] + matrix[2][0])):   
            continue
        else:
            solutions.append(matrix)

print(solutions) 

                

                    

