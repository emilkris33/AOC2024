
def mix(val, sec):
    return val ^ sec

def prune(sec):
    return sec % 16777216

def next_secret(sec):
    sec = prune(mix(sec * 64, sec))
    sec = prune(mix(int(sec / 32), sec))
    return prune(mix(sec * 2048, sec))

def task1():
    global secrets
    input_file = open("input.txt")
    secrets = [int(n) for n in input_file.readlines()]

    total = 0
    for secret in secrets:
        for _ in range(2000):
            secret = next_secret(secret)
        total += secret
    return total


def task2():
    buys = {}
    for secret in secrets:
        price = secret % 10
        changes = []
        buys_in_round = []
        for _ in range(2000):
            new_secret = next_secret(secret)
            new_price = new_secret % 10
            change = new_price - price
            changes.append(change)
            secret = new_secret
            price = new_price
            if len(changes) >= 4:
                sequence = (changes[-4], changes[-3], changes[-2], changes[-1])
                if sequence in buys_in_round:
                    continue
                if sequence not in buys:
                    buys[sequence] = price
                else:
                    buys[sequence] += price
                buys_in_round.append(sequence)
    return max(buys.values())

if __name__ == '__main__':
    print(task1())
    print(task2())