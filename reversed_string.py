a_string = input("enter a string:")
a_word_list = a_string.split()
print(a_word_list)
the_gener = (s for s in a_word_list[::-1])
for s in the_gener:
    print(s,end=' ')
print('\n')