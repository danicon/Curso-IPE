ultimo = 10
fila = list(range(1,ultimo+1))

while True:
    print(f"Existem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao final da fila. ")
    print("ou A para realizar o atendimento. S para sair ")
    operacao = input("Operação (F, A ou S): ")
    if operacao == 'A' or operacao == 'a':
        if len(fila) > 0:
            atendimento = fila.pop(0)
            print(f"Cliente {atendimento} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operacao == 'F' or operacao == 'f':
        ultimo += 1
        fila.append(ultimo)
    elif operacao == 'S' or operacao == 's':
        print("\n Até mais... \n")
        break
    else:
        print("Operação invalida! Digite apenas F, A ou S")