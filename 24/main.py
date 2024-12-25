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
    global wires
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
    true_result = a_value+b_value
    #print(f"{(a_value+b_value):b}")
    #print(f"{result:b}")
    first_result = result

    output = []

    swap1 = [['sgt', 'gbv'], ['sgt', 'kch'], ['tgq', 'gbv'], ['tgq', 'kch'], ['z11', 'gbv'], ['z11', 'dgv'], ['z11', 'kch'], ['z11', 'dpg'], ['z11', 'hpr'], ['qts', 'gbv'], ['qts', 'kch'], ['kvg', 'gbv'], ['kvg', 'kch'], ['dwh', 'gbv'], ['dwh', 'kch'], ['tvp', 'gbv'], ['tvp', 'kch'], ['dcr', 'gbv'], ['dcr', 'kch'], ['kmb', 'gbv'], ['kmb', 'kch'], ['gbv', 'mmf'], ['gbv', 'z16'], ['gbv', 'kks'], ['gbv', 'sjm'], ['gbv', 'z25'], ['dgv', 'mmf'], ['dgv', 'z16'], ['dgv', 'z25'], ['mmf', 'kch'], ['mmf', 'dpg'], ['mmf', 'hpr'], ['z16', 'kch'], ['z16', 'dpg'], ['z16', 'hpr'], ['kks', 'kch'], ['sjm', 'kch'], ['kch', 'z25'], ['z25', 'dpg'], ['z25', 'hpr']]
    swap2 = [['qts', 'gbs', 'sgt', 'gbv'], ['qts', 'fsh', 'sgt', 'gbv'], ['qts', 'z10', 'sgt', 'gbv'], ['kvg', 'gbs', 'sgt', 'gbv'], ['kvg', 'fsh', 'sgt', 'gbv'], ['kvg', 'z10', 'sgt', 'gbv'], ['dwh', 'gbs', 'sgt', 'gbv'], ['dwh', 'fsh', 'sgt', 'gbv'], ['dwh', 'z15', 'sgt', 'gbv'], ['dwh', 'z10', 'sgt', 'gbv'], ['tvp', 'gbs', 'sgt', 'gbv'], ['tvp', 'fsh', 'sgt', 'gbv'], ['tvp', 'z15', 'sgt', 'gbv'], ['tvp', 'z10', 'sgt', 'gbv'], ['dcr', 'gbs', 'sgt', 'gbv'], ['dcr', 'fsh', 'sgt', 'gbv'], ['dcr', 'z10', 'sgt', 'gbv'], ['gbs', 'z16', 'sgt', 'gbv'], ['gbs', 'sjm', 'sgt', 'gbv'], ['gbs', 'z25', 'sgt', 'gbv'], ['mmf', 'fsh', 'sgt', 'gbv'], ['mmf', 'z15', 'sgt', 'gbv'], ['mmf', 'z10', 'sgt', 'gbv'], ['tsw', 'z16', 'sgt', 'gbv'], ['tsw', 'z25', 'sgt', 'gbv'], ['z35', 'z16', 'sgt', 'gbv'], ['z35', 'z25', 'sgt', 'gbv'], ['fsh', 'z16', 'sgt', 'gbv'], ['fsh', 'sjm', 'sgt', 'gbv'], ['fsh', 'z25', 'sgt', 'gbv'], ['z15', 'z16', 'sgt', 'gbv'], ['z15', 'z25', 'sgt', 'gbv'], ['z16', 'z10', 'sgt', 'gbv'], ['sjm', 'z10', 'sgt', 'gbv'], ['z25', 'z10', 'sgt', 'gbv']]
    swap3 = [['fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['z15', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['z25', 'z10', 'qts', 'gbs', 'sgt', 'gbv']]
    swap4 = [['ctd', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['hwr', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['bnw', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['kvd', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['mbt', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['hng', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['mqf', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['qhw', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['rwt', 'z10', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['z10', 'bhk', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv'], ['z10', 'dkm', 'fsh', 'z25', 'qts', 'gbs', 'sgt', 'gbv']]

    if False:
        for swap in swap3:
            swap_candidates = [key for key in wires if key[0] not in ['x', 'y'] and key not in swap]
            for v1, v2 in combinations(swap_candidates, 2):
                wires = {}
                new_result = task1([v1, v2, swap[0], swap[1], swap[2], swap[3], swap[4], swap[5]])
                if new_result is None:
                    continue
                if (new_result ^ true_result).bit_count() < 1:
                    #print(f"swap {v1} and {v2}")
                    output.append([v1, v2, swap[0], swap[1], swap[2], swap[3], swap[4], swap[5]])
                    swaps = [v1, v2, swap[0], swap[1], swap[2], swap[3], swap[4], swap[5]]
                    swaps.sort()
                    for s in swaps:
                        print(s, end=',')
                    print()
            return output

    for swap in swap4:
        wires = {}
        new_result = task1(swap, "input_changed.txt")
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

        swap.sort()
        if new_result == true_result:
            for s in swap:
                print(s, end=',')
            print()



if __name__ == '__main__':
    print(task1())
    print(task2())