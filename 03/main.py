import re

def task1():
    input_file = open("input.txt")
    input_text = input_file.read()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", input_text)
    total = 0
    for match in matches:
        f1, f2 = match[4:-1].split(',')
        total += int(f1)*int(f2)
    return total


def task2():
    input_file = open("input.txt")
    input_text = input_file.read()
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input_text)
    total = 0
    do = True
    for match in matches:
        if match == "do()":
            do = True
            continue
        if match == "don't()":
            do = False
            continue
        if do:
            f1, f2 = match[4:-1].split(',')
            total += int(f1)*int(f2)
    return total

if __name__ == '__main__':
    print(task1())
    print(task2())