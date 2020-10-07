'''

# Lista - nome_lista.append (valor)

# Lista - nome_lista.insert (index , valor)


DIFERENÇA
ENTRE APPEND E INSERT

append Insere um novo elemento no final da lista Tem apenas um argumento (valor a inserir)

insert Insere um novo elemento em qualquer posição Tem dois argumentos ( valor)

'''

import os
os.system('cls')
print("\n")

list_valor = []

x=0
while(x<3):
    list_valor.append(float(input(f"Numero {x+1}:")) )
    x = x+1

print("Apresenta lista \n")
x=0
while(x<3):
    print("{0}".format(list_valor[x] )+ "\n")
    x=x+1


#del list_valor[len(list_valor)-1] # Apaga o  último elemento da lista

del list_valor[0]

print("Apresenta lista com o último indice removido \n") 

x=0
while(x<len(list_valor)):
    print("{0}".format(list_valor[x] )+ "\n")
    x=x+1