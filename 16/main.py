directions = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}

grid = []


def pos_string(pos):
    return f"{pos[0]},{pos[1]},{pos[2]}"

def compare_pos(pos1, pos2):
    return pos1[0] == pos2[0] and pos1[1] == pos2[1]

def add_pos(pos1, pos2):
    return [pos1[0] + pos2[0] , pos1[1] + pos2[1]]

def task1():
    global came_from
    global end
    global g_score
    input_file = open("input.txt")
    for i, line in enumerate(input_file.readlines()):
        grid.append([n for n in line.strip()])
        if 'S' in line:
            start = [i, line.find('S'), '>']
        if 'E' in line:
            end = [i, line.find('E'), None]

    to_search = [start]
    came_from = {}

    g_score = {pos_string(start): 0}

    while len(to_search) > 0:
        to_search.sort(key=lambda pos: g_score[pos_string(pos)], reverse=True)
        current = to_search.pop()
        current_str = pos_string(current)
        if compare_pos(current, end):
            return g_score[current_str]

        for direction in directions:
            if direction == current[2]:
                next = [current[0] + directions[direction][0] , current[1] + directions[direction][1], direction]
                temp_g_score = g_score[current_str] + 1
            else:
                next = [current[0], current[1], direction]
                temp_g_score = g_score[current_str] + 1000

            if grid[next[0]][next[1]] == '#':
                continue

            next_str = pos_string(next)
            if next_str not in g_score or temp_g_score < g_score[next_str]:
                came_from[next_str] = [current]
                g_score[next_str] = temp_g_score
                if next not in to_search:
                    to_search.append(next)
            elif temp_g_score == g_score[next_str]:
                came_from[next_str].append(current)

def pos_string_2(pos):
    return f"{pos[0]},{pos[1]}"

def task2():
    on_path = [pos_string_2(end)]

    to_consider = [[end[0], end[1], direction] for direction in directions]
    to_consider = [n for n in to_consider if pos_string(n) in g_score]
    while len(to_consider) > 0:
        current = to_consider.pop()
        if pos_string_2(current) not in on_path:
            on_path.append(pos_string_2(current))
        if pos_string(current) in came_from:
            to_consider.extend(came_from[pos_string(current)])
    return len(on_path)


if __name__ == '__main__':
    print(task1())
    print(task2())