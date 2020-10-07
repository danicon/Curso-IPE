lista_at = []
soma = 0
media = 0

x = 0
while x<8:
    lista_at.insert(x, float(input(f"Entre com a altura {x+1}:")))
    soma += lista_at[x] 
    x+=1
media = soma / len(lista_at)
print(f"A media das 8 alturas é {media}")