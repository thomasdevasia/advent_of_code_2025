# read the input file
def read_input(file_path: str) -> list[str]:
    lines = []
    with open(file_path, "r") as file:
        for line in file:
            lines.append(line.strip())
    return lines


def find_largest_joltage(input_data: list[str]) -> list[int]:
    results = []
    for line in input_data:
        largest_loc = -1
        temp_result = ""
        battery_len = 12
        while battery_len > 0:
            largest = 0
            for i in range(largest_loc + 1, len(line) - battery_len + 1):
                if largest < int(line[i]):
                    largest = int(line[i])
                    largest_loc = i
            temp_result += str(largest)
            battery_len -= 1
        results.append(int(temp_result))
    return results


# file_path = "./input_test.txt"
file_path = "./input.txt"
input_data = read_input(file_path)
# print(input_data)

result = find_largest_joltage(input_data)
# print(result)
print(sum(result))
