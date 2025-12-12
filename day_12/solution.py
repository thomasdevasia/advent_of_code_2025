def read_input(filename):
    shapes = {}
    shapes_flag = True
    regions = []
    with open(filename, "r") as file:
        idx = 0
        for line in file:
            if "x" in line:
                shapes_flag = False
            if shapes_flag and ":" in line:
                idx = int(line.split(":")[0])
                # shapes[idx] = []
                shapes[idx] = 0
            if shapes_flag and ("." in line or "#" in line):
                # shapes[idx].append(line.strip())
                temp_count = 0
                for char in line.strip():
                    if char == "#":
                        temp_count += 1
                shapes[idx] += temp_count
            if not shapes_flag and "x" in line:
                temp = line.strip().split()
                width = int(temp[0].removesuffix(":").split("x")[0])
                length = int(temp[0].removesuffix(":").split("x")[1])
                quant = [int(temp[j]) for j in range(1, len(temp))]
                regions.append((width, length, quant))
    return shapes, regions


def solution(input_shapes, input_regions):
    counter = 0
    for grid_r, grid_c, quant in input_regions:
        total_grid_size = grid_r * grid_c
        total_size_covered = sum([n * input_shapes[i] for i, n in enumerate(quant)])
        print(total_grid_size, total_size_covered * 1.3)
        if total_size_covered * 1.3 < total_grid_size:
            counter += 1
    print("counter: ", counter)


path = "input.txt"
# path = "input_test.txt"

input_shapes, input_regions = read_input(path)
print("Shapes:", input_shapes)
print("Regions:", input_regions)

solution(input_shapes, input_regions)
