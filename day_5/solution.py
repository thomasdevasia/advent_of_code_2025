# read input
def read_input(file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    fresh_id_range = []
    available_id = []
    flag = False
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                flag = True
                continue
            if flag:
                available_id.append(int(line))
            else:
                temp = line.split("-")
                fresh_id_range.append((int(temp[0]), int(temp[1])))
    return fresh_id_range, available_id


def check_in_range(id: int, fresh_id_range: list[tuple[int, int]]) -> bool:
    for min_id, max_id in fresh_id_range:
        if min_id <= id <= max_id:
            return True
    return False


def find_fresh_ids(
    fresh_id_range: list[tuple[int, int]], available_id: list[int]
) -> int:
    result = 0
    for id in available_id:
        if check_in_range(id, fresh_id_range):
            result += 1
    return result


path = "./input.txt"
# path = "./input_test.txt"

fresh_id_range, available_id = read_input(path)

result = find_fresh_ids(fresh_id_range, available_id)
print(f"Result: {result}")
