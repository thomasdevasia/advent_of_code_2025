# read input
def read_input(file_path: str) -> list[list[str]]:
    results = []
    with open(file_path, "r") as f:
        for line in f:
            temp = line.strip().split()
            results.append(temp)
    return results


def calc_sum(input_data: list[list[str]]) -> int:
    len_x = len(input_data[0])
    len_y = len(input_data)
    result = 0
    for x in range(len_x):
        temp_list = []
        temp = 0
        for y in range(len_y):
            if y == len_y - 1:
                if input_data[y][x] == "*":
                    temp = 1
                    for item in temp_list:
                        temp *= int(item)
                    # print(temp)
                if input_data[y][x] == "+":
                    temp = 0
                    for item in temp_list:
                        temp += int(item)
                    # print(temp)
            else:
                temp_list.append(input_data[y][x])
        result += temp
    return result


# path = "./input_test.txt"
path = "./input.txt"
input_data = read_input(path)
# print(input_data)

result = calc_sum(input_data)
print(result)
