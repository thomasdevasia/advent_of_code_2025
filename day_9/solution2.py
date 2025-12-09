def read_input(filename: str) -> list[tuple[int, int]]:
    results = []
    with open(filename, "r") as file:
        for line in file:
            c = int(line.strip().split(",")[0])
            r = int(line.strip().split(",")[1])
            results.append((c, r))
    return results


def tile_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    width = abs(p2[0] - p1[0]) + 1
    height = abs(p2[1] - p1[1]) + 1
    return width * height


def largest_area(inputs: list[tuple[int, int]]) -> int:
    max_area = 0
    for i in range(len(inputs)):
        for j in range(i + 1, len(inputs)):
            area = tile_area(inputs[i], inputs[j])
            # print(f"Area between {inputs[i]} and {inputs[j]}: {area}")
            if area > max_area:
                max_area = area
    return max_area


# path = "input.txt"
path = "input_test.txt"
input_data = read_input(path)
# print(input_data)

result = largest_area(input_data)
print(f"Largest area: {result}")
