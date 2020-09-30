vezes = 0
while vezes <= 104:
    
    print("digite 1 para soma:")
    print("digite 2 para subitracao:")
    print("digite 3 para multiplicacao:")
    print("digite 4 para divisao:")
    print("digite 5 para sair:")

    numero_digitado = int(input("digite aqui:"))

    if numero_digitado == 1:
        valor_digitado1 = (float(input("digite o primeiro numero a ser calculado:")))
        valor_digitado2 = (float(input("digite o segundo numero a ser calculado:")))
        print("O resultado de {} + {} = {}".format(valor_digitado1,valor_digitado2, valor_digitado1 + valor_digitado2))

    elif numero_digitado == 2:
        valor_digitado1 = (float(input("digite o primeiro numero a ser calculado:")))
        valor_digitado2 = (float(input("digite o segundo numero a ser calculado:")))
        print("O resultado de {} - {} = {}".format(valor_digitado1,valor_digitado2, valor_digitado1 - valor_digitado2))

    elif numero_digitado == 3:
        valor_digitado1 = (float(input("digite o primeiro numero a ser calculado:")))
        valor_digitado2 = (float(input("digite o segundo numero a ser calculado:")))
        print("O resultado de {} * {} = {}".format(valor_digitado1,valor_digitado2, valor_digitado1 * valor_digitado2))

    elif numero_digitado == 4:
        valor_digitado1 = (float(input("digite o primeiro numero a ser calculado:")))
        valor_digitado2 = (float(input("digite o segundo numero a ser calculado:")))
        print("O resultado de {} / {} = {}".format(valor_digitado1,valor_digitado2, valor_digitado1 / valor_digitado2))

    elif numero_digitado == 5:
        vezes = 105
        print("ate a proxima ;)")

    else:
        print("valor digitado invalido  tente novamento...")

vezes +=1