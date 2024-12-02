
def is_report_safe(levels):
    direction = (levels[1] - levels[0]) > 0
    for i in range(len(levels) - 1):
        if not 1 <= abs(levels[i + 1] - levels[i]) <= 3:
            return False
        if (levels[i + 1] - levels[i] > 0) != direction:
            return False
    return True

def task1():
    input_file = open("input.txt")
    num_safe = 0
    for line in input_file.readlines():
        levels = [int(n) for n in line.split(' ')]
        if is_report_safe(levels):
            num_safe += 1
    return num_safe

def task2():
    input_file = open("input.txt")
    num_safe = 0
    for line in input_file.readlines():
        levels = [int(n) for n in line.split(' ')]
        if is_report_safe(levels):
            num_safe += 1
        else:
            for i in range(len(levels)):
                new_report = levels.copy()
                new_report.pop(i)
                if is_report_safe(new_report):
                    num_safe += 1
                    break
    return num_safe

if __name__ == '__main__':
    print(task1())
    print(task2())