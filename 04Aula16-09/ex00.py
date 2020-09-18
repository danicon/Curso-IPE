tabu = 1
num = 1
while tabu <= 10:
    print('%d x %d = %d' % (tabu, num, tabu * num))
    num += 1
    if num == 11:
        num = 1
        tabu += 1