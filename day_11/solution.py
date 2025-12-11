import sys


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


def find_path(input_data, curr_path, start=False):
    # print(f"Visiting: {curr_path}")
    if curr_path == "you" and not start:
        return 0
    if curr_path == "out":
        return 1
    result = 0
    for path in input_data[curr_path]:
        result += find_path(input_data, path)
    return result


# path = "input.txt"
path = "input_test.txt"
input_data = read_input(path)
# print(input_data)

result = find_path(input_data, "you", True)
print(f"Result: {result}")
