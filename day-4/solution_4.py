def parse_range_pair(line: str) -> list:
    ranges = line.split(sep=",")
    parsed_ranges = list()
    for single_range in ranges:
        range_limits = single_range.split(sep="-")
        parsed_ranges.append((int(range_limits[0]), int(range_limits[1])))
    return parsed_ranges


def does_range_pair_fully_overlap(range_pair: list) -> bool:
    first_lower, first_upper = range_pair[0][0], range_pair[0][1]
    second_lower, second_upper = range_pair[1][0], range_pair[1][1]
    if first_lower >= second_lower and first_upper <= second_upper:
        return True
    elif second_lower >= first_lower and second_upper <= first_upper:
        return True
    else:
        return False


def read_range_pairs(input_path="./input.txt") -> list:
    with open(input_path, "r") as input_data:
        return [parse_range_pair(line) for line in input_data]


def count_fully_overlaping_pairs(range_pairs: list) -> int:
    return sum(
        1 for range_pair in range_pairs if does_range_pair_fully_overlap(range_pair)
    )


def main():
    range_pairs = read_range_pairs()
    print(count_fully_overlaping_pairs(range_pairs))


if __name__ == "__main__":
    main()
