# read input
def read_input(file_path: str) -> list[str]:
    results = []
    with open(file_path, "r") as f:
        for line in f:
            results.append(line.removesuffix("\n"))
    return results


def calc_sum(input_data: list[str]) -> int:
    result = 0
    len_y = len(input_data)
    operators = input_data[len_y - 1].strip().split()
    num_list = input_data[0 : len_y - 1]
    len_y -= 1
    # print(operators)
    # print(num_list)
    temp_list = []
    for line in num_list:
        for i in range(len(line)):
            # print(f"i: {i}, line[i]: {line[i]}")
            if i < len(temp_list):
                temp = temp_list[i]
                temp += line[i]
                temp_list[i] = temp
            else:
                temp = ""
                temp += line[i]
                temp_list.append(temp)
    temp_list2 = []
    for item in temp_list:
        if item == " " * len(item):
            continue
        temp_list2.append(int(item.strip()))
    # print(temp_list2)
    for i in range(len(operators)):
        start_pos = i * len_y
        last_pos = start_pos + len_y
        print(f"operator: {operators[i]}, list: {temp_list2[start_pos:last_pos]}")
        if operators[i] == "+":
            temp = 0
        else:
            temp = 1
        for digit in temp_list2[start_pos:last_pos]:
            if operators[i] == "+":
                temp += digit
            if operators[i] == "*":
                temp *= digit
        result += temp
    return result


# path = "./input_test.txt"
path = "./input.txt"
input_data = read_input(path)
# print(input_data)

result = calc_sum(input_data)
print(f"result: {result}")
