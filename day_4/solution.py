# read input
def read_input(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def check_valid(input: list[list[str]], x: int, y: int) -> bool:
    # print(f"Checking {input[x][y]} at {x},{y}")
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    count = 0
    len_x = len(input)
    len_y = len(input[0])
    for direction in directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        if new_x < 0 or new_x >= len_x or new_y < 0 or new_y >= len_y:
            continue
        if input[new_x][new_y] != ".":
            count += 1
        if count >= 4:
            return False
    return True


def solve(input: list[str]) -> int:
    grid = [list(line) for line in input]
    result = 0
    for i in range(len(grid)):
        # print(f"{grid[i]}")
        for j in range(len(grid[i])):
            if grid[i][j] == "@" and check_valid(grid, i, j):
                grid[i][j] = "x"
                # print(f"Valid at {i},{j}")
                result += 1

    # print("\nFinal grid:")
    # for line in grid:
    #     print("".join(line))
    return result


# input_path = "./input_test.txt"
input_path = "./input.txt"

input_data = read_input(input_path)
# for line in input_data:
#     print(line)

result = solve(input_data)
print(f"Result: {result}")
