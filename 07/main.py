from numpy.ma.core import outer


def perform_step(value, numbers):
    if len(numbers) == 1:
        return value == numbers[0]
    return perform_step(value, [numbers[0]+numbers[1]]+numbers[2:]) or perform_step(value, [numbers[0]*numbers[1]]+numbers[2:])

def task1():
    input_file = open("input.txt")
    output = 0
    for line in input_file.readlines():
        value, numbers = line.split(':')
        value = int(value)
        numbers = [int(n) for n in numbers.strip().split(' ')]
        if perform_step(value, numbers):
            output += value
    return output

def perform_step_2(value, numbers):
    if len(numbers) == 1:
        return value == numbers[0]
    return perform_step_2(value, [numbers[0]+numbers[1]]+numbers[2:]) or perform_step_2(value, [numbers[0]*numbers[1]]+numbers[2:]) or perform_step_2(value, [int(str(numbers[0])+str(numbers[1]))]+numbers[2:])

def task2():
    input_file = open("input.txt")
    output = 0
    for line in input_file.readlines():
        value, numbers = line.split(':')
        value = int(value)
        numbers = [int(n) for n in numbers.strip().split(' ')]
        if perform_step_2(value, numbers):
            output += value
    return output

if __name__ == '__main__':
    print(task1())
    print(task2())