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


def find_fresh_ids(fresh_id_range: list[tuple[int, int]]) -> int:
    result = 0
    sorted_ranges = sorted(fresh_id_range, key=lambda x: x[0])
    new_ranges = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = new_ranges[-1]
        if start <= last_end + 1:
            new_ranges[-1] = (last_start, max(last_end, end))
        else:
            new_ranges.append((start, end))
    for start, end in new_ranges:
        result += end - start + 1
    return result


path = "./input.txt"
# path = "./input_test.txt"

fresh_id_range, available_id = read_input(path)

result = find_fresh_ids(fresh_id_range)
print(f"Result: {result}")
