# read input
def read_input(file_path: str) -> list[list[str]]:
    results = []
    with open(file_path, "r") as f:
        for line in f:
            temp = [char for char in line]
            temp.remove("\n")
            results.append(temp)
    return results


def convert_operator_num(
    input_data: list[list[str]],
) -> tuple[list[list[int]], list[str]]:
    len_x = len(input_data[0])
    len_y = len(input_data)
    num = ""
    operator_list = []
    num_list = []
    temp_list = []
    for x in range(len_x):
        for y in range(len_y):
            # print(f"X: {x}, Y: {y}")
            if y == len_y - 1:
                if input_data[y][x] == "+" or input_data[y][x] == "*":
                    operator_list.append(input_data[y][x])
                continue
            num += input_data[y][x]
            if y == len_y - 2:
                temp = num.strip()
                num = ""
                if temp == "":
                    num_list.append(temp_list)
                    temp_list = []
                elif x == len_x - 1:
                    temp_list.append(int(temp))
                    num_list.append(temp_list)
                    temp_list = []
                else:
                    temp_list.append(int(temp))
    # print(operator_list)
    # print(num_list)
    return num_list, operator_list


def calculate_expression(num_list: list[list[int]], operator_list: list[str]) -> int:
    total = 0
    for i in range(len(num_list)):
        if operator_list[i] == "+":
            temp = 0
        else:
            temp = 1
        for num in num_list[i]:
            if operator_list[i] == "+":
                temp += num
            if operator_list[i] == "*":
                temp *= num
        # print(f"Operator: {operator_list[i]}, Numbers: {num_list[i]}, total: {temp}")
        total += temp
    return total


# path = "./input_test.txt"
path = "./input.txt"
input_data = read_input(path)
# print(input_data)
# for line in input_data:
#     print(line)

num_list, operator_list = convert_operator_num(input_data)
# print(num_list)

result = calculate_expression(num_list, operator_list)
print(f"Result: {result}")
