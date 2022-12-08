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


def count_seeable_tres(tree_height: int, tree_slice: np.ndarray):
    seeable = 0
    for tree in tree_slice:
        seeable += 1
        if tree >= tree_height:
            break
    return seeable


def find_best_scenic_score(trees: np.ndarray) -> int:
    best_score = 0
    for i, tree_row in enumerate(trees):
        for j, tree in enumerate(tree_row):
            right_seeable = count_seeable_tres(tree, trees[i, j + 1 :])
            left_seeable = count_seeable_tres(tree, np.flip(trees[i, :j]))
            bottom_seeable = count_seeable_tres(tree, trees[i + 1 :, j])
            top_seeable = count_seeable_tres(tree, np.flip(trees[:i, j]))
            scenic_score = right_seeable * left_seeable * bottom_seeable * top_seeable
            if scenic_score > best_score:
                best_score = scenic_score
    return best_score


def main():
    trees = read_trees()
    num_visible = count_visible_trees(trees)
    best_score = find_best_scenic_score(trees)
    utils.write_answers_to_file(num_visible, best_score, file_name="answer_8.txt")
    print(num_visible, best_score)


if __name__ == "__main__":
    main()
