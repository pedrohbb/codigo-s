#1
dic = {"AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia", "CE": "Ceará", "ES": "Espírito Santo",
"GO": "Goiás", "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul", "MG": "Minas Gerais", "PA": "Pará", 
"PB": "Paraíba", "PR":"Paraná", "PI":"Piauí", "RJ":"Rio de Janeiro", "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul", 
"RO": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins", "DF": "Distrito Federal"}

estado = input("Escreva a sigla do estado desejado: ")

print(dic[estado])


#2
dic = {"história": 70, "geografia": 75, "português": 70, "matemática": 100, "física": 95, "química": 80}
keys = list(dic.keys())
val = list(dic.values())
val_ord = []
dic_ord = {}

#-----criar uma lista em ordem decrescente-----#
for i in range(len(val)):
    val_ord = val_ord + [max(val)]
    val.remove(max(val))

#-----associar cada valor a sua respectiva key seguindo a ordem imposta porw val_ord-----# 
for i in range(len(val_ord)):
    for j in range(len(keys)):
        if (val_ord[i] != dic[keys[j]]) or (keys[j] in dic_ord):
            continue
# sem a condição adicional acima, as chaves cujos valores se repetem 'n' vezes serão associadas 'n' vezes ao mesmo valor
        else:
            dic_ord[keys[j]] = val_ord[i] 
         
print(dic_ord)

#2 - solução alternativa (menos intuitiva)

dic = {"história": 70, "geografia": 75, "português": 70, "matemática": 100, "física": 95, "química": 80}
keys = list(dic.keys())
val = list(dic.values())
dic_ord = {}

for i in range(len(val)):
    for j in range(len(keys)):
        if max(val) != dic[keys[j]]:
            continue
        elif keys[j] in dic_ord:
            continue
        else:
            dic_ord[keys[j]] = max(val)          
    val.remove(max(val))

print(dic_ord)
