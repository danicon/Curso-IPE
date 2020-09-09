a=10
b=5
c=a*b

mgs ="\n A Multiplicação de " + str(a) + " x " + str(b) + " = " + str(c) + "\n"
mgs1 = " \n A Multiplicação de {0} x {1} = {2}".format(a, b, c)
print(mgs)

print(mgs1)