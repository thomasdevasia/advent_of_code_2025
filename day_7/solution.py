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


def move(start_pos: list[list[str]], x: int, y: int) -> None:
    new_y = y + 1
    # print_grid(grid)
    # print("len x:{len_x} len y:{len_y}".format(len_x=len(grid[0]), len_y=len(grid)))
    # print(f"Moving to X:({x}, Y:{new_y})")
    if new_y < len(grid) and grid[new_y][x] == ".":
        grid[new_y][x] = "|"
        move(grid, x, new_y)
    elif new_y < len(grid) and grid[new_y][x] == "^":
        if x - 1 >= 0 and grid[new_y][x - 1] == ".":
            grid[new_y][x - 1] = "|"
            move(grid, x - 1, new_y)
        if x + 1 < len(grid[0]) and grid[new_y][x + 1] == ".":
            grid[new_y][x + 1] = "|"
            move(grid, x + 1, new_y)
    else:
        pass


def find_splits(grid: list[list[str]]) -> int:
    count = 0
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "^":
                top_x = j
                top_y = i - 1
                if top_x >= 0 and grid[top_y][top_x] == "|":
                    count += 1
    return count


path = "input.txt"
# path = "input_test.txt"
grid = read_input(path)
# print_grid(grid)

start_pos = find_start(grid)
# print(f"Start position: {start_pos}")

move(grid, start_pos[1], start_pos[0])
# print("final grid")
# print_grid(grid)

result = find_splits(grid)
print(f"Number of splits: {result}")
