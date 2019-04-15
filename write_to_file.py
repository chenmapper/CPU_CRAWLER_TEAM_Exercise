filepath = '/Users/panxuanyou/Desktop/'

filename = 'write.txt'

list1 = [2,3,4,5,3,2,4]

with open(filepath + filename, 'w') as f:
    for el in list1:
        f.write(str(el) + ' ')
        print(el, 'is written to the file')