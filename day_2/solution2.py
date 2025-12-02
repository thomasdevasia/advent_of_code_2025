# read from input.txt
def read_input(file_path: str):
    with open(file_path, "r") as file:
        return file.read().replace("\n", "").split(",")


def chec_valid(val: int):
    temp = str(val)
    # if len(temp) % 2 != 0:
    # return False
    for i in range(len(temp) // 2):
        pattern = temp[: i + 1]
        pattern_match = True
        # print(f"pattern: {pattern}")
        for j in range(0, len(temp), i + 1):
            # print(f"comparing with: {temp[j : j + i + 1]}")
            if pattern != temp[j : j + i + 1]:
                pattern_match = False
                break
        if pattern_match:
            return True
    return False


def find_invalid(input_data: list[str]):
    sum = 0
    for item in input_data:
        min, max = item.split("-")
        print(min, max)
        for i in range(int(min), int(max) + 1):
            # print(f"Checking number: {i}")
            if chec_valid(i):
                # print(f"Found palindrome: {i}")
                sum += i
    return sum


# input_data = read_input("input_test.txt")
input_data = read_input("input.txt")
print(input_data)

result = find_invalid(input_data)
print("Result:", result)
