#357686312646216567629137
#        2646216567629137
import math
import time

def is_prime(num):
    if num%2 == 0 and num != 2:
        print('not a prime number.')
    else:
        if num == 1:
            print('not a prime')
        else:
            if num in (2, 3):
                print('prime')
            else:
                flag = 1
                for n in range(1, int(math.sqrt(num) + 1)): #+1 # prime n^p * m^q * o^r ...
                    if num % n == 0 and n != 1:
                        print('not prime')
                        flag = 0
                        break
                if flag:
                    print('prime')

def is_prime2(num):
    if num in (0,1):
        print('not prime')
    elif num in (2,3):
        print('prime')
    else:
        flag = 1
        for n in range(2,num): #don't need to +1
            if num%n == 0:
                print('not prime')
                flag = 0
                break
        if flag:
            print('prime')


def main():
    number = input("enter:")
    print(time.time())
    is_prime(int(number))
    print(time.time())

    print('-------------------------')

    number = input("enter:")
    print(time.time())
    is_prime2(int(number))
    print(time.time())

if __name__ == '__main__':
    main()

