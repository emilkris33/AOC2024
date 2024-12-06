import math
rules = []
wrong_orders = []

def task1():
    input_file = open("input.txt")
    output = 0
    for line in input_file.readlines():
        if '|' in line:
            n1, n2 = line.split('|')
            rules.append([int(n1), int(n2)])
            continue
        if len(line) == 1:
            continue
        order = [int(n) for n in line.split(',')]
        for rule in rules:
            if rule[0] in order and rule[1] in order:
                if order.index(rule[0]) > order.index(rule[1]):
                    wrong_orders.append(order)
                    break
        else:
            output += order[math.floor(len(order)/2)]
    return output


def task2():
    output = 0
    swaps = 0
    for order in wrong_orders:
        while True:
            for rule in rules:
                if rule[0] in order and rule[1] in order:
                    idx_0 = order.index(rule[0])
                    idx_1 = order.index(rule[1])
                    if idx_0 > idx_1:
                        order[idx_0], order[idx_1] = order[idx_1], order[idx_0]
                        swaps += 1
                        break
            else:
                break
        output += order[math.floor(len(order) / 2)]
    print(f"Total number of swaps: {swaps}")
    return output

if __name__ == '__main__':
    print(task1())
    print(task2())