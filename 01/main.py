import numpy as np

list_left = []
list_right = []

def task1():
    input_file = open("input.txt")
    for line in input_file.readlines():
        split = line.split(' ')
        list_left.append(int(split[0]))
        list_right.append(int(split[-1]))
    list_left.sort()
    list_right.sort()

    total = 0
    for n1, n2 in zip(list_left, list_right):
        total += abs(n1-n2)

    print(total)

def task2():
    total = 0
    list_right_np = np.array(list_right)
    for n in list_left:
        total += n * sum(list_right_np == n)

    print(total)

if __name__ == '__main__':
    task1()
    task2()