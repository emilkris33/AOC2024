import math
import re

def is_whole(f, eps=0.0001):
    return abs(f - round(f)) < abs(eps)

def task1():
    input_file = open("input.txt")
    total = 0
    for line in input_file.readlines():
        if len(line.strip()) == 0:
            continue
        m = [int(n) for n in re.search(r"^\D+(\d+)\D+(\d+)", line).groups()]
        if line.startswith("Button A:"):
            A = m
        elif line.startswith("Button B:"):
            B = m
        elif line.startswith("Prize: X"):
            C = m
            v0 = (C[0] / B[0] - C[1] / B[1]) / (A[0] / B[0] - A[1] / B[1])
            v1 = (C[0] / A[0] - C[1] / A[1]) / (B[0] / A[0] - B[1] / A[1])
            if not is_whole(v0) or not is_whole(v1):
                continue
            v0 = round(v0)
            v1 = round(v1)
            if v1 < 0 or v0 < 0:
                continue
            assert C[0] == A[0]*v0+B[0]*v1
            assert C[1] == A[1]*v0+B[1]*v1
            total += v0*3 + v1
    return total


def task2():
    input_file = open("input.txt")
    total = 0
    for line in input_file.readlines():
        if len(line.strip()) == 0:
            continue
        m = [int(n) for n in re.search(r"^\D+(\d+)\D+(\d+)", line).groups()]
        if line.startswith("Button A:"):
            A = m
        elif line.startswith("Button B:"):
            B = m
        elif line.startswith("Prize: X"):
            C = [n+10000000000000 for n in m]
            v0 = (C[0] / B[0] - C[1] / B[1]) / (A[0] / B[0] - A[1] / B[1])
            v1 = (C[0] / A[0] - C[1] / A[1]) / (B[0] / A[0] - B[1] / A[1])
            if not is_whole(v0) or not is_whole(v1):
                continue
            v0 = round(v0)
            v1 = round(v1)
            if v1 < 0 or v0 < 0:
                continue
            assert C[0] == A[0]*v0+B[0]*v1
            assert C[1] == A[1]*v0+B[1]*v1
            total += v0*3 + v1
    return total

if __name__ == '__main__':
    print(task1())
    print(task2())