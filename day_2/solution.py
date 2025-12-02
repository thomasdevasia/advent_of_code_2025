# read from input.txt
def read_input(file_path: str):
    with open(file_path, "r") as file:
        return file.read().replace("\n", "").split(",")


def chec_valid(val: int):
    temp = str(val)
    return len(temp) % 2 == 0 and temp[: len(temp) // 2] == temp[len(temp) // 2 :]


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
            # if int(temp[: length // 2]) == int(temp[length // 2 :]):
            #     print(f"Found palindrome: {temp}")
            #     sum += 1
        # print("-----")
    return sum


# input_data = read_input("input_test.txt")
input_data = read_input("input.txt")
print(input_data)

result = find_invalid(input_data)
print("Result:", result)
