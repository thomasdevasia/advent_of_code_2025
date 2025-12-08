import math
from collections import defaultdict


def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            result.append([int(x) for x in line.strip().split(",")])
    return result


def euclidean_distance(
    point1: tuple[int, int, int], point2: tuple[int, int, int]
) -> float:
    return math.sqrt(
        (point1[0] - point2[0]) ** 2
        + (point1[1] - point2[1]) ** 2
        + (point1[2] - point2[2]) ** 2
    )


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # no change; already in same circuit
        # Union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def solve(input_data, num_connection) -> None:
    edges: list[tuple[float, int, int]] = []
    for i in range(len(input_data)):
        for j in range(i + 1, len(input_data)):
            point1 = input_data[i]
            point2 = input_data[j]
            dist = euclidean_distance(point1, point2)
            edges.append((dist, i, j))
    edges.sort(key=lambda x: x[0])
    dsu = UnionFind(num_connection)
    limit = min(num_connection, len(edges))
    for k in range(limit):
        _, i, j = edges[k]
        dsu.union(i, j)
    component_count = defaultdict(int)
    for i in range(len(input_data)):
        parent = dsu.find(i)
        component_count[parent] += 1
    sizes = sorted(component_count.values(), reverse=True)
    if len(sizes) < 3:
        raise ValueError("Less than 3 components found.")
    product = sizes[0] * sizes[1] * sizes[2]
    print(f"Sizes of first three components: {sizes[0]}, {sizes[1]}, {sizes[2]}")
    print(f"Product of sizes: {product}")


# path = "./input_test.txt"
path = "./input.txt"
input_data = read_input(path)
# print(input_data)


solve(input_data, 1000)

