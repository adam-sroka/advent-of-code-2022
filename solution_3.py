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
INPUT_PATH = "inputs/input_3.txt"

from utils import utils


def get_item_priority(item: str) -> int:
    priority = PRIORITIES[item.lower()]
    if item.isupper():
        priority += 26
    return priority


def find_duplicate_items(items: str) -> str:
    half_length = len(items) // 2
    first_compartment_items = items[:half_length]
    second_compartment_items = items[half_length:]
    duplicates = list(filter(lambda item: item in first_compartment_items, second_compartment_items))
    return duplicates[0]


def find_badge_item(group: list) -> str:
    possible_items = [
        *PRIORITIES.keys(),
        *[letter.upper() for letter in PRIORITIES.keys()],
    ]
    group_rucksack_items = [set(rucksack) for rucksack in group]
    for item in possible_items:
        if all(item in items for items in group_rucksack_items):
            return item
    raise ValueError("No badge item found")


def read_rucksacks(input_path: str = INPUT_PATH) -> list:
    with open(input_path, "r") as input_data:
        return [line.strip() for line in input_data]


def get_groups(rucksacks: list) -> list:
    i = iter(rucksacks)
    return list(zip(i, i, i))


def sum_duplicate_item_priorities(rucksacks):
    return sum([get_item_priority(find_duplicate_items(items)) for items in rucksacks])


def sum_badge_item_priorities(groups):
    return sum([get_item_priority(find_badge_item(group)) for group in groups])


def main():
    rucksacks = read_rucksacks()
    duplicate_items_priorities_sum = sum_duplicate_item_priorities(rucksacks)
    groups = get_groups(rucksacks)
    badge_items_priorities_sum = sum_badge_item_priorities(groups)
    utils.write_answers_to_file(duplicate_items_priorities_sum, badge_items_priorities_sum, file_name="answer_3.txt")
    print(duplicate_items_priorities_sum, badge_items_priorities_sum)


if __name__ == "__main__":
    main()
