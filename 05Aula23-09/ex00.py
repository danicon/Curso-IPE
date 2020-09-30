import os
os.system("cls")

print("\n \n")
# 89-55-34-21-13-8-5-3-2-1-1-0
inicio = 89
proximo = 55
message = ""

# print(inicio)
# print(proximo)
while(inicio >= 0): 
    
    aux = inicio - proximo
    inicio = proximo
    proximo = aux

    if (aux == 0):
        message += f"{aux}"
        inicio = -1
    else:
        message += f"{aux} - "

print(f"89 - 55 - " + message + "\n\n")
