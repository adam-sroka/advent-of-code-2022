INPUT_PATH = "inputs/input_9.txt"

from utils import utils


def update_tail_pos(new_head_pos: tuple, curr_tail_pos: tuple) -> tuple:
    new_head_x = new_head_pos[0]
    new_head_y = new_head_pos[1]
    curr_tail_x = curr_tail_pos[0]
    curr_tail_y = curr_tail_pos[1]

    # if touching (distance less than two), don't move
    if ((new_head_x - curr_tail_x) ** 2 + (new_head_y - curr_tail_y) ** 2) ** 0.5 < 2:
        return curr_tail_pos

    # if on same hor/ver line, move closer by one step
    if new_head_x == curr_tail_x:
        if new_head_y > curr_tail_y:
            new_tail_pos = (curr_tail_x, curr_tail_y + 1)
        elif new_head_y < curr_tail_y:
            new_tail_pos = (curr_tail_x, curr_tail_y - 1)
        else:
            new_tail_pos = curr_tail_pos
    if new_head_y == curr_tail_y:
        if new_head_x > curr_tail_x:
            new_tail_pos = (curr_tail_x + 1, curr_tail_y)
        elif new_head_x < curr_tail_x:
            new_tail_pos = (curr_tail_x - 1, curr_tail_y)
        else:
            new_tail_pos = curr_tail_pos

    # if away diagonally, move diagonally
    if new_head_x > curr_tail_x and new_head_y > curr_tail_y:
        new_tail_pos = (curr_tail_x + 1, curr_tail_y + 1)
    if new_head_x < curr_tail_x and new_head_y > curr_tail_y:
        new_tail_pos = (curr_tail_x - 1, curr_tail_y + 1)
    if new_head_x > curr_tail_x and new_head_y < curr_tail_y:
        new_tail_pos = (curr_tail_x + 1, curr_tail_y - 1)
    if new_head_x < curr_tail_x and new_head_y < curr_tail_y:
        new_tail_pos = (curr_tail_x - 1, curr_tail_y - 1)

    # TODO maybe check if their distance is within one?
    return new_tail_pos


def read_head_motions(input_path: str = INPUT_PATH):
    motions = list()
    with open(input_path) as input_data:
        lines = input_data.read().splitlines()
    for line in lines:
        split_line = line.split()
        for _ in range(int(split_line[1])):
            motions.append(split_line[0])
    return motions


def update_head_pos(curr_head_pos, motion):
    if motion == "R":
        return (curr_head_pos[0] + 1, curr_head_pos[1])
    elif motion == "L":
        return (curr_head_pos[0] - 1, curr_head_pos[1])
    elif motion == "U":
        return (curr_head_pos[0], curr_head_pos[1] + 1)
    elif motion == "D":
        return (curr_head_pos[0], curr_head_pos[1] - 1)
    else:
        raise (ValueError("Invalid motion"))


def get_tail_path(head_motions: list, rope_length: int = 2) -> list:
    rope_positions = [(0, 0) for _ in range(rope_length)]
    tail_path_coords = [rope_positions[-1]]
    for motion in head_motions:
        for i, pos in enumerate(rope_positions):
            if i == 0:  # head
                rope_positions[i] = update_head_pos(pos, motion)
            else:
                rope_positions[i] = update_tail_pos(rope_positions[i - 1], pos)
            tail_path_coords.append(rope_positions[-1])
    return tail_path_coords


def get_unique_path_positions(path: list) -> int:
    return len(set(path))


def main():
    head_motions = read_head_motions()
    tail_path = get_tail_path(head_motions)
    long_tail_path = get_tail_path(head_motions, rope_length=10)
    unique_tail_positions = get_unique_path_positions(tail_path)
    unique_long_tail_positions = get_unique_path_positions(long_tail_path)
    utils.write_answers_to_file(unique_tail_positions, unique_long_tail_positions, file_name="answer_9.txt")
    print(unique_tail_positions, unique_long_tail_positions)


if __name__ == "__main__":
    main()
