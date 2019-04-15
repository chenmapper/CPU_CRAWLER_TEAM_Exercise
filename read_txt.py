filepath = '/Users/panxuanyou/Desktop/read.txt' #content: 34 23 5 11 2 6 34

f = open(filepath, 'r')

print('The content of the file is: ', f.read())

f.close()