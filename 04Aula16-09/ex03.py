fibona = 89
anterior = 34

while fibona > 0:
    print(fibona)
    fibona -= anterior
    anterior = fibona - anterior

    if fibona == 0:
        print(fibona)