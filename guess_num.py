import random





answer_num = random.randint(1,9)
number = int(input("enter:"))
while number != answer_num:
    if number < answer_num:
        number = int(input('too small, try again:'))
    elif number > answer_num:
        number = int(input('too big, try again:'))
print('bingo')

for i in range(50):
    print(random.randint(1,9))