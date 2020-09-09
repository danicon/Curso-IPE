qt_cigarrod = int(input("Digite a quantidade de cigarros: "))
anos_fumo = int(input("Quantidade de anos fumados: "))

dias_fumos_vida = anos_fumo * 365
cigarros_consumido = dias_fumos_vida * qt_cigarrod
minutos_perdidos = cigarros_consumido * 10
minutos = 24 * 60
dias_perdidos = minutos_perdidos / minutos

print("Você já perdeu {0}".format(round(dias_perdidos,2)) + " da sua vida")