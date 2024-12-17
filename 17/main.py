import re
from pstats import Stats
from urllib.request import proxy_bypass_registry


class Computer:
    def __init__(self, a, b, c, program):
        self.A = a
        self.B = b
        self.C = c
        self.P = program
        self.p = 0
        self.running = True

    def combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        raise Exception

    def step(self):
        opcode = self.P[self.p]
        operand = self.P[self.p + 1]
        match opcode:
            case 0: #adv
                self.A = int(self.A / (2**self.combo(operand)))
            case 1: #bxl
                self.B ^= operand
            case 2: #bst
                self.B = self.combo(operand) % 8
            case 3: #jnz
                if self.A != 0:
                    self.p = operand
                else:
                    self.p += 2
            case 4: #bxc
                self.B ^= self.C
            case 5: #out
                self.p += 2
                return self.combo(operand)%8
            case 6: #bdv
                self.B = int(self.A / (2**self.combo(operand)))
            case 7: #cdv
                self.C = int(self.A / (2**self.combo(operand)))

        if opcode != 3:
            self.p += 2
        if self.p >= len(self.P):
            self.running = False
        return None



def task1():
    input_file = open("input.txt")
    for line in input_file.readlines():
        if line.startswith("Register A:"):
            A_start = int(re.findall(r"\d+", line)[0])
        elif line.startswith("Register B:"):
            B_start = int(re.findall(r"\d+", line)[0])
        elif line.startswith("Register C:"):
            C_start = int(re.findall(r"\d+", line)[0])
        elif line.startswith("Program:"):
            program = [int(n) for n in re.findall(r"\d+", line)]

    com = Computer(A_start, B_start, C_start, program)
    while com.running:
        o = com.step()
        if o is not None:
            print(o, end=',')



def task2():
    input_file = open("input.txt")
    for line in input_file.readlines():
        if line.startswith("Register A:"):
            A_start = int(re.findall(r"\d+", line)[0])
        elif line.startswith("Register B:"):
            B_start = int(re.findall(r"\d+", line)[0])
        elif line.startswith("Register C:"):
            C_start = int(re.findall(r"\d+", line)[0])
        elif line.startswith("Program:"):
            program = [int(n) for n in re.findall(r"\d+", line)]

    V = 4652658759614

    for x in range(1000):
        for y in range(1000):
            A_start = x * V + y
            com = Computer(A_start, B_start, C_start, program)
            output = []
            while com.running:
                o = com.step()
                if o is not None:
                    output.append(o)
            for i in range(len(output)):
                if output[-(i+1)] != program[-(i+1)]:
                    break
            else:
                print(f"{A_start=}, {len(output)=}")


if __name__ == '__main__':
    task1()
    print()
    print(task2())