from itertools import combinations
from tkinter.constants import NORMAL

from colorama.ansi import clear_screen

initial_values = {}
gates = []
wires = {}

class Wire:
    def __init__(self, name):
        self.name = name
        self.output = []
        self.input = None
        self.value = None

    def set_output(self, gate):
        self.output.append(gate)

    def set_input(self, gate):
        if self.input is not None:
            raise Exception
        self.input = gate

    def set_value(self, value):
        if self.value is not None:
            raise Exception
        self.value = value
        for gate in self.output:
            gate.set_input(value)

class Gate:
    def __init__(self, in1, in2, op, out):
        if in1 not in wires:
            wires[in1] = Wire(in1)
        if in2 not in wires:
            wires[in2] = Wire(in2)
        if out not in wires:
            wires[out] = Wire(out)

        wires[in1].set_output(self)
        wires[in2].set_output(self)
        self.op = op
        wires[out].set_input(self)
        self.output = wires[out]
        self.input_wires = [in1, in2]

        self.inputs = []

    def set_input(self, value):
        self.inputs.append(value)
        if len(self.inputs) == 1:
            return
        if len(self.inputs) > 2:
            raise Exception
        match self.op:
            case "AND":
                self.output.set_value(self.inputs[0] & self.inputs[1])
            case "OR":
                self.output.set_value(self.inputs[0] | self.inputs[1])
            case "XOR":
                self.output.set_value(self.inputs[0] ^ self.inputs[1])



def task1(to_swap = None, file="input.txt"):
    input_file = open(file)
    for line in input_file.readlines():
        if ':' in line:
            wire, value = line.split(':')
            initial_values[wire] = int(value)
        elif ">" in line:
            elements = line.strip().split(' ')
            if to_swap is None or elements[4] not in to_swap:
                Gate(elements[0], elements[2], elements[1], elements[4])
            else:
                swap_pos = to_swap.index(elements[4])
                if swap_pos % 2 == 0:
                    swap_pos += 1
                else:
                    swap_pos -= 1
                Gate(elements[0], elements[2], elements[1], to_swap[swap_pos])

    for wire, value in initial_values.items():
        wires[wire].set_value(value)

    output_wires = [key for key in wires if key[0] == 'z']
    output_wires.sort(reverse=True)
    global result
    result = 0
    for key in output_wires:
        if wires[key].value is None:
            return None
        result <<= 1
        result += wires[key].value
    return result



def task2():
    swaps = ["z10", "kmb", "z15", "tvp", "z25", "dpg", "mmf", "vdk"]
    global wires
    wires = {}
    task1(swaps)

    printed = []
    for i in range(46):
        point_of_interest = f"z{i:>02}"

        to_consider = [point_of_interest]
        while len(to_consider) > 0:
            wire_name = to_consider.pop(0)
            if wire_name[0] in ['x', 'y']:
                continue
            if wire_name in printed:
                continue
            printed.append(wire_name)
            wire = wires[wire_name]
            print(f"{wire.name} = {wire.input.input_wires[0]} {wire.input.op} {wire.input.input_wires[1]}")
            to_consider.extend(wire.input.input_wires)
        print()

    a_wires = [key for key in wires if key[0] == 'x']
    a_wires.sort(reverse=True)
    a_value = 0
    for key in a_wires:
        a_value <<= 1
        a_value += wires[key].value

    b_wires = [key for key in wires if key[0] == 'y']
    b_wires.sort(reverse=True)
    b_value = 0
    for key in b_wires:
        b_value <<= 1
        b_value += wires[key].value
    true_result = a_value + b_value
    print(f"{(true_result):b}")
    print(f"{result:b}")

    swaps.sort()
    output = ""
    for swap in swaps:
        output += swap + ","
    return output


if __name__ == '__main__':
    print(task1())
    print(task2())