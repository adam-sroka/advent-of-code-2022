INPUT_PATH = "inputs/input_7.txt"

from utils import utils


def find_dirs_sizes(input_path: str = INPUT_PATH) -> dict():
    curr_path = list()  # stack
    dirs_sizes = dict()
    add_sizes_to_this_path = dict()
    with open(input_path) as input_data:
        for line in input_data:
            split_line = line.split()
            is_command = split_line[0] == "$"
            if is_command:
                is_cd = split_line[1] == "cd"
                is_ls = split_line[1] == "ls"
                if is_cd:
                    is_base_dir = split_line[2] == "/"
                    is_cd_up = split_line[2] == ".."
                    if is_base_dir:
                        curr_path = ["/"]
                    elif is_cd_up:
                        curr_path.pop()
                    else:  # cd to subdir
                        curr_path.append(split_line[2])
                elif is_ls:
                    if tuple(curr_path) in add_sizes_to_this_path:  # TODO change to defaultdict
                        add_sizes_to_this_path[tuple(curr_path)] = False
                    else:
                        add_sizes_to_this_path[tuple(curr_path)] = True
            else:  # is output
                is_file = split_line[0].isdigit()
                if is_file:
                    file_size = int(split_line[0])
                    # add file size to current dir and all its parents
                    # only if we have run ls for the first time in this path
                    if add_sizes_to_this_path[tuple(curr_path)]:
                        for index, _ in enumerate(curr_path):
                            if tuple(curr_path[: index + 1]) in dirs_sizes:  # TODO change to defaultdict
                                dirs_sizes[tuple(curr_path[: index + 1])] += file_size
                            else:
                                dirs_sizes[tuple(curr_path[: index + 1])] = file_size

    return dirs_sizes


def sum_dirs_under_size(dirs_sizes: dict, max_size: int = 100000):
    return sum([dir_size for dir_size in dirs_sizes.values() if dir_size < max_size])


def main():
    dirs_sizes = find_dirs_sizes()
    dirs_sizes_under_size = sum_dirs_under_size(dirs_sizes)
    utils.write_answers_to_file(dirs_sizes_under_size, file_name="answer_7.txt")
    print(dirs_sizes_under_size)


if __name__ == "__main__":
    main()
