PRIORITIES = {
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
}


def get_item_priority(item: str) -> int:
    priority = PRIORITIES[item.lower()]
    if item.isupper():
        priority += 26
    return priority


def find_duplicate_items(items: str) -> str:
    half_length = len(items) // 2
    first_compartment_items = items[:half_length]
    second_compartment_items = items[half_length:]
    duplicates = list(
        filter(lambda item: item in first_compartment_items, second_compartment_items)
    )
    return duplicates[0]


def read_rucksacks(input_path="./input.txt") -> list:
    with open(input_path, "r") as input_data:
        return [line.strip() for line in input_data]


def sum_duplicate_item_priorities(rucksacks):
    return sum([get_item_priority(find_duplicate_items(items)) for items in rucksacks])


def write_answers(answers: list, path="./answer.txt") -> None:
    with open(path, "w") as answer_data:
        for answer in answers:
            answer_data.write(str(answer))
            answer_data.write("\n")


def main():
    rucksacks = read_rucksacks()
    priorities_sum = sum_duplicate_item_priorities(rucksacks)
    write_answers([priorities_sum])
    print(priorities_sum)


if __name__ == "__main__":
    main()
