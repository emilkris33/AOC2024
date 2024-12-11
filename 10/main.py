grid = []
total_trails = 0
peaks = []

def climb(i, j, n):
    global total_trails
    global peaks
    if (not 0 <= i < len(grid)) or (not 0 <= j < len(grid[0])) or grid[i][j] != n:
        return
    if n == 9:
        total_trails += 1
        peak_id = f"{i},{j}"
        if peak_id not in peaks:
            peaks.append(peak_id)
        return
    climb(i-1, j, n+1)
    climb(i+1, j, n+1)
    climb(i, j-1, n+1)
    climb(i, j+1, n+1)

def task1():
    global peaks
    input_file = open("input.txt")
    for line in input_file.readlines():
        grid.append([int(n) for n in line.strip()])

    sum_peaks = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                continue
            peaks = []
            climb(i,j,0)
            sum_peaks += len(peaks)
    return sum_peaks

def task2():
    return total_trails

if __name__ == '__main__':
    print(task1())
    print(task2())