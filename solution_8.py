INPUT_PATH = "inputs/input_8.txt"

import numpy as np
from utils import utils


def read_trees(input_path: str = INPUT_PATH) -> np.ndarray:
    with open(input_path) as input_data:
        lines = input_data.read().splitlines()
        trees = [np.array(list(map(int, line)), dtype=int) for line in lines]
        return np.array(trees)


def count_visible_trees(trees: np.ndarray) -> int:
    num_visible = 0
    for i, tree_row in enumerate(trees):
        for j, tree in enumerate(tree_row):
            visible_from_left = all(trees[i, :j] < tree)
            visible_from_right = all(trees[i, j + 1 :] < tree)
            visible_from_top = all(trees[:i, j] < tree)
            visible_from_bottom = all(trees[i + 1 :, j] < tree)
            if visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
                num_visible += 1
    return num_visible


def main():
    trees = read_trees()
    num_visible = count_visible_trees(trees)
    utils.write_answers_to_file(num_visible, file_name="answer_8.txt")
    print(num_visible)


if __name__ == "__main__":
    main()
