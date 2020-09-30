# Faça uma solução lógica em Python que leia o número de termos, determine e mostre os valores de acordo com a série a seguir:
# Série = 7, 2, 3, 1, 21, 4, 12, 5, 63, 8, 48, 25, 189, 16, 192, 125, 567, 32, 768, 625...

primeiro = 7
segundo = 2 
terceiro = 3
quarto = 1
msg = ''
while quarto != 625:
    primeiro = primeiro * 3
    segundo = segundo * 2
    terceiro = terceiro * 4
    quarto = quarto * 5

    if quarto == 625:
        msg += f"{primeiro}, {segundo}, {terceiro}, {quarto}..."
    else:
        msg += f"{primeiro}, {segundo}, {terceiro}, {quarto}, "

print(f"7, 2, 3, 1, " + msg)