import math

numbers = None
value_in_store = {}

def value_in(n, i):
    if i == 0:
        return 1
    if n not in value_in_store:
        value_in_store[n] = {}
    if i not in value_in_store[n]:
        n_len = math.ceil(math.log10(n+1))
        if n == 0:
            value_in_store[n][i] = value_in(1, i-1)
        elif n_len % 2 == 0:
            pow10 = 10**(n_len/2)
            n1 = int(n/pow10)
            n2 = n % pow10
            value_in_store[n][i] = value_in(n1, i - 1) + value_in(n2, i - 1)
        else:
            value_in_store[n][i] = value_in(n*2024, i - 1)
    return value_in_store[n][i]


def task1():
    global numbers
    input_file = open("input.txt")
    line = input_file.readline()
    numbers = [int(n) for n in line.split(' ')]

    total = 0
    for number in numbers:
        total += value_in(number, 25)
    return total

def task2():
    total = 0
    for number in numbers:
        total += value_in(number, 75)
    return total

if __name__ == '__main__':
    print(task1())
    print(task2())