prato = 5
pilha = list(range(1,prato+1))

while True:
    print(f"\nExistem {len(pilha)} pratos na PILHA")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato ")
    print("ou D para desenpilhar. S para sair ")
    operacao = input("Operação (E, D ou S): ")
    if operacao == 'D':
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! Nada para lavar")
    elif operacao == "E":
        prato += 1
        pilha.append(prato)
    elif operacao == "S":
        print('\n Até mais... \n')
        break
    else:
        print("Operação invalida! Digite apenas E, D ou S") 