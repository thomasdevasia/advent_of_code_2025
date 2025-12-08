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
    n = len(input_data)
    for i in range(n):
        for j in range(i + 1, n):
            point1 = input_data[i]
            point2 = input_data[j]
            dist = euclidean_distance(point1, point2)
            edges.append((dist, i, j))
    edges.sort(key=lambda x: x[0])
    dsu = UnionFind(num_connection)
    components = n
    last_merge_edge = None

    for _, i, j in edges:
        if dsu.union(i, j):
            components -= 1
            last_merge_edge = (i, j)
            if components == 1:
                break
    if last_merge_edge:
        print(f"Last merge edge: {last_merge_edge}")
        i, j = last_merge_edge
        x1 = input_data[i][0]
        x2 = input_data[j][0]
        print(f"Last merge edge x-coordinates: {x1}, {x2}")
        print(f"Product of last merge edge x-coordinates: {x1 * x2}")


# path = "./input_test.txt"
path = "./input.txt"
input_data = read_input(path)
# print(input_data)


solve(input_data, 1000)
