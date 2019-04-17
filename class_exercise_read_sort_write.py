fin = open('/Users/panxuanyou/Desktop/in.txt', 'r')

list_origin = fin.read().split(' ')

fin.close()

for i in range(len(list_origin)):
     list_origin[i] = int(list_origin[i])

print(list_origin)

for i in range(len(list_origin)):
    for j in range(len(list_origin)):
        if list_origin[j] > list_origin[i]:
            list_origin[j], list_origin[i] = list_origin[i], list_origin[j]

print(list_origin)

fout = open('/Users/panxuanyou/Desktop/sort.txt', 'w')

for i in list_origin:
    fout.write(str(i) + ' ')

fout.close()

