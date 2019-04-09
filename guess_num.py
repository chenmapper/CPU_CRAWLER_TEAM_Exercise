import random



alist = [i for i in range(1,10) if i%2==0]

answer_num = random.randint(1,9)
while num != answer_num:
    number = int(input("enter:"))
    if number < answer_num:
        number = input('too small, try again:')
    else if number > answer_num:
        number = input('too big, try again:')
    els