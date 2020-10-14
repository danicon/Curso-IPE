list1 = [1, 3, 7, 6, 5]
list2 = ['olá', 'oi', 'blz', 'ok', 'opá']
list3 = []

a=0
for i in list1:
    list3.append(list1[a])
    list3.append(list2[a])
    a+=1
print(list3)