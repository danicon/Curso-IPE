lista = [10, 17, 3]
print(" Apresenta o valor da lista - 1 \n")
x=0
while(x<3):
    print(f"{lista[x]}")
    x+=1

print(" Solicite valores para a lista - 1 \n")

x=0
while(x<3):
    lista[x] = float(input(f"Números {x+1}:"))
    x+=1

print(" Apresenta o valor lista - 2 \n")

x=0
while(x<3):
    print(f"{lista[x]}")
    x+=1