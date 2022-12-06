INPUT_PATH = "inputs/input_4.txt"

from utils import utils


def parse_range_pair(line: str) -> list:
    ranges = line.split(sep=",")
    parsed_ranges = list()
    for single_range in ranges:
        range_limits = single_range.split(sep="-")
        parsed_ranges.append((int(range_limits[0]), int(range_limits[1])))
    return parsed_ranges


def get_range_pair_boundaries(range_pair: list) -> tuple:
    first_lower, first_upper = range_pair[0][0], range_pair[0][1]
    second_lower, second_upper = range_pair[1][0], range_pair[1][1]
    return first_lower, first_upper, second_lower, second_upper


def does_range_pair_fully_overlap(range_pair: list) -> bool:
    first_lower, first_upper, second_lower, second_upper = get_range_pair_boundaries(range_pair)
    is_first_in_second = first_lower >= second_lower and first_upper <= second_upper
    is_second_in_first = second_lower >= first_lower and second_upper <= first_upper
    if is_first_in_second or is_second_in_first:
        return True
    return False


def does_range_pair_overlap(range_pair: list) -> bool:
    first_lower, first_upper, second_lower, second_upper = get_range_pair_boundaries(range_pair)
    is_first_lower_in_second = first_lower >= second_lower and first_lower <= second_upper
    is_second_lower_in_first = second_lower >= first_lower and second_lower <= first_upper
    if is_first_lower_in_second or is_second_lower_in_first:
        return True
    return False


def read_range_pairs(input_path: str = INPUT_PATH) -> list:
    with open(input_path, "r") as input_data:
        return [parse_range_pair(line) for line in input_data]


def count_overlaping_pairs(range_pairs: list, fully=True) -> int:
    overlap_check = does_range_pair_fully_overlap if fully else does_range_pair_overlap
    return sum(map(lambda range_pair: overlap_check(range_pair), range_pairs))


def main():
    range_pairs = read_range_pairs()
    full_overlaps_num = count_overlaping_pairs(range_pairs)
    partial_overlaps_num = count_overlaping_pairs(range_pairs, fully=False)
    utils.write_answers_to_file(full_overlaps_num, partial_overlaps_num, file_name="answer_4.txt")
    print(full_overlaps_num, partial_overlaps_num)


if __name__ == "__main__":
    main()
