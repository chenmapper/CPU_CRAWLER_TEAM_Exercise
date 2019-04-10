import time


def time_decorator(func):
    def wrapper(length):
        t1 = time.time()
        func(length)
        t2 = time.time()
        print(t2-t1)
        print('-------------------')

    return wrapper


@time_decorator
def fib(length):
    fib_list = [1, 1]
    while length < 2:
        fib_list.pop()
        length += 1
    if length > 2:
        for i in range(2, length):
            fib_list.append(fib_list[i - 2] + fib_list[i - 1])
    #print(fib_list)


# for resolution
@time_decorator
def fib2(length):
    fib_list = [1,1]
    if length ==1:
        print([1])
    elif length == 2:
        print([1,1])
    else:
        a,b = (1,1)
        for i in range(2,length):
            a,b = b,a+b
            fib_list.append(b)
        #print(fib_list)

# recursive resolution
@time_decorator
def fib3(length):
    def fib_calculate(n):
        if n in (1, 2):
            return int(1)
        else:
            return fib_calculate(n-2) + fib_calculate(n-1)

    fib_list = []
    for i in range(1,length+1):
        fib_list.append(fib_calculate(i))
    #print(fib_list)


length = int(input("enter a number of fib's length:"))

fib(length)
fib2(length)
fib3(length)
