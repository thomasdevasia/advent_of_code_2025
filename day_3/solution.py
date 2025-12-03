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
        largest = 0
        largest_loc = 0
        second_largest = 0

        for i in range(len(line) - 1):
            if int(line[i]) > largest:
                largest = int(line[i])
                largest_loc = i
        # print(f"Largest: {largest} at {largest_loc}")

        for i in range(largest_loc + 1, len(line)):
            if second_largest < int(line[i]):
                second_largest = int(line[i])
        # print(f"Second Largest: {second_largest}")

        results.append((10 * largest) + second_largest)

    return results


# file_path = "./input_test.txt"
file_path = "./input.txt"
input_data = read_input(file_path)
print(input_data)

result = find_largest_joltage(input_data)
print(sum(result))
