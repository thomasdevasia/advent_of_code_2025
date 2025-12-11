import sys
from functools import cache


def read_input(filename):
    result = {}
    with open(filename, "r") as file:
        for line in file:
            rack_name = line.strip().split(":")[0]
            paths = line.strip().split(":")[1].strip().split()
            if rack_name not in result:
                result[rack_name] = paths
            else:
                print(f"Duplicate rack name found: {rack_name}")
                sys.exit(1)
    return result


def check_visited(visited):
    dac = False
    fft = False
    for path in visited:
        if path == "dac":
            dac = True
        if path == "fft":
            fft = True
    return dac and fft


@cache
def find_path(curr_path, dac, fft, start=False):
    # print(f"Visiting: {curr_path}")
    new_dac = dac
    new_fft = fft
    if curr_path == "dac":
        new_dac = True
    if curr_path == "fft":
        new_fft = True
    if curr_path == "svr" and not start:
        return 0
    if curr_path == "out":
        if new_dac and new_fft:
            print("  Valid path found!")
            return 1
        else:
            return 0
    result = 0
    for path in input_data[curr_path]:
        result += find_path(path, new_dac, new_fft)
    return result


path = "input.txt"
# path = "input_test2.txt"
input_data = read_input(path)
# print(input_data)

result = find_path("svr", False, False, True)
print(f"Result: {result}")
