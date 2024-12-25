computers = {}

class Computer:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def connect(self, other):
        if other not in self.connections:
            self.connections.append(other)
            other.connections.append(self)



def task1():
    input_file = open("input.txt")

    for line in input_file.readlines():
        name1, name2 = line.strip().split('-')
        if name1 not in computers:
            computers[name1] = Computer(name1)
        if name2 not in computers:
            computers[name2] = Computer(name2)

        computers[name1].connect(computers[name2])

    sets_of_three = []
    for i, name in enumerate(computers):
        computer = computers[name]
        for j, con1 in enumerate(computer.connections):
            intersection = list(set(computer.connections) & set(con1.connections))
            for con2 in intersection:
                names = [name, con1.name, con2.name]
                names.sort()
                names = (names[0], names[1], names[2])
                if names not in sets_of_three:
                    sets_of_three.append(names)

    total = 0
    for pc_set in sets_of_three:
        if pc_set[0][0] == 't' or pc_set[1][0] == 't' or pc_set[2][0] == 't':
            total += 1
    return total



def task2():
    biggest_party = []
    for computer in computers.values():
        party = set(computer.connections) | {computer}
        for con in computer.connections:
            intersection = set(computer.connections) & set(con.connections) | {computer, con}
            if len(intersection) < 8:
                continue
            party &= intersection
        if len(party) > len(biggest_party):
            biggest_party=party
    biggest_party = list(biggest_party)
    biggest_party.sort(key=lambda c: c.name)
    out = ""
    for c in biggest_party:
        out += c.name + ","
    out = out[:-1]
    return out

if __name__ == '__main__':
    print(task1())
    print(task2())