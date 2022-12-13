from collections import deque
import numpy as np
from utils import utils


INPUT_PATH = "inputs/input_12.txt"
HEIGHTS = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "S": 0,
    "E": 27,
}


class Node:
    def __init__(self):
        self.reachable_neighbours = None
        self.symbol = None

    def is_start(self):
        if self.symbol == "S":
            return True
        else:
            return False

    def is_end(self):
        if self.symbol == "E":
            return True
        else:
            return False


class HeightMap:
    def __init__(self):
        self.raw_heights = None
        self.height_map = {}
        self.start_pos = None
        self.end_pos = None

    def load_raw_heights(self, input_path=INPUT_PATH):
        with open(input_path) as input_data:
            self.raw_heights = input_data.read().splitlines()

    def decode_raw_heights(self):
        heights = np.array(
            [np.array(list(map(lambda char: HEIGHTS[char], line)), dtype=int) for line in self.raw_heights]
        )
        shape = heights.shape
        for j, row in enumerate(heights):
            for i, height in enumerate(row):
                correction = 0
                if height == 0:
                    self.start_pos = (j, i)
                    correction = 1
                elif height == 27:
                    self.end_pos = (j, i)
                    correction = -1
                reachable_nodes = []
                real_height = height + correction
                if i - 1 >= 0 and heights[j, i - 1] <= real_height + 1:
                    reachable_nodes.append((j, i - 1))
                if i + 1 < shape[1] and heights[j, i + 1] <= real_height + 1:
                    reachable_nodes.append((j, i + 1))
                if j - 1 >= 0 and heights[j - 1, i] <= real_height + 1:
                    reachable_nodes.append((j - 1, i))
                if j + 1 < shape[0] and heights[j + 1, i] <= real_height + 1:
                    reachable_nodes.append((j + 1, i))
                self.height_map[(j, i)] = reachable_nodes

    def find_shortest_path_distance(self):  # bfs
        to_search = deque()
        to_search.append((0, self.start_pos))
        searched = []
        while to_search:
            distance, node = to_search.popleft()
            if node not in searched:
                if node == self.end_pos:
                    return distance
                else:
                    for neighbour in self.height_map[node]:
                        to_search.append((distance + 1, neighbour))
                    searched.append(node)


def main():
    terrain = HeightMap()
    terrain.load_raw_heights()
    terrain.decode_raw_heights()
    distance = terrain.find_shortest_path_distance()
    utils.write_answers_to_file(distance, file_name="answer_12.txt")
    print(distance)


if __name__ == "__main__":
    main()
