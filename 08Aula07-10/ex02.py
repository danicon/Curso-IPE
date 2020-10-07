list1 = []
list2 = []
list3 = []

print('\nLista 1 \n')
x=0
while x < 6:
    list1.append(float(input(f"Numero {x+1}: ")) )
    x = x+1
print(f"{list1}")

print("\nLista 2 \n")

x=0
while x < 6:
    list2.append(float(input(f"Numero {x+1}: ")) )
    x = x+1
print(f"{list2}")

x=0
y=0
while x < 6:
    list3.insert(y, list1[x])
    y+=1
    list3.insert(y, list2[x])
    y+=1
    x+=1
print(list3)