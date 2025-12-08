import copy


def read_input(filename: str) -> list[list[str]]:
    result = []
    with open(filename, "r") as file:
        temp = []
        for line in file:
            temp = [char for char in line.strip()]
            result.append(temp)
    return result


def find_start(grid: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "S":
                return (i, j)
    raise ValueError("Start position 'S' not found in the grid.")


def print_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print(line)
    print("-----")


def move(grid: list[list[str]], x: int, y: int) -> None:
    if y >= len(grid):
        # print_grid(grid)
        global count
        count += 1
        # print(f"Count: {count}")
        return
    if x < 0 or x >= len(grid[0]):
        return
    if grid[y][x] == "^":
        move(copy.deepcopy(grid), x - 1, y)
        move(copy.deepcopy(grid), x + 1, y)
        return
    elif grid[y][x] == ".":
        grid[y][x] = "|"
    move(copy.deepcopy(grid), x, y + 1)


path = "input.txt"
# path = "input_test.txt"
input_grid = read_input(path)
# print_grid(input_grid)

start_pos = find_start(input_grid)
# print(f"Start position: {start_pos}")

count = 0
move(input_grid, start_pos[1], start_pos[0])
print(f"Final count: {count}")
