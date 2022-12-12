from typing import List, Tuple, Dict
from copy import deepcopy
from math import lcm

INPUT_PATH = "inputs/input_11.txt"


class Monkey:
    def __init__(
        self,
        id: int,
        items: List[int],
        operation: Tuple,
        div_test_by: int,
        div_true_monkey_id: int,
        div_false_monkey_id: int,
    ):
        self.id = id
        self.items = items
        self.operation = operation
        self.div_test_by = div_test_by
        self.div_true_monkey_id = div_true_monkey_id
        self.div_false_monkey_id = div_false_monkey_id
        self.inspected_num = 0

    def __repr__(self):
        return f"Monkey {self.id} with items: {self.items}, doing: {self.operation}, throwing to {self.div_true_monkey_id} if divisble by {self.div_test_by}, else to {self.div_false_monkey_id}."

    def _operate(self, item):
        if self.operation[0] == "+":
            return item + self.operation[1]
        elif self.operation[0] == "*":
            return item * self.operation[1]
        elif self.operation[0] == "**":
            return item ** self.operation[1]

    def inspect(self, modulus=None):
        self.items = [self._operate(item) for item in self.items]
        if modulus is not None:
            self.items = [item % modulus for item in self.items]
        self.inspected_num += len(self.items)

    def relieve(self):
        self.items = [item // 3 for item in self.items]

    def throw_items(self):
        items_thrown_to_monkeys = {}
        for item in self.items:
            if item % self.div_test_by == 0:
                # TODO use defaultdict
                if self.div_true_monkey_id in items_thrown_to_monkeys:
                    items_thrown_to_monkeys[self.div_true_monkey_id].append(item)
                else:
                    items_thrown_to_monkeys[self.div_true_monkey_id] = [item]
            else:
                if self.div_false_monkey_id in items_thrown_to_monkeys:
                    items_thrown_to_monkeys[self.div_false_monkey_id].append(item)
                else:
                    items_thrown_to_monkeys[self.div_false_monkey_id] = [item]
        self.items = []  # threw away all items
        return items_thrown_to_monkeys


class MonkeyInTheMiddle:
    def __init__(self):
        self.monkeys = []

    def read_monkeys(self, input_path: str = INPUT_PATH):
        with open(input_path) as input_data:
            lines = input_data.read().splitlines()
        for line in lines:
            split_line = line.split()
            if len(split_line) == 0:
                pass
            elif split_line[0] == "Monkey":
                monkey_id = int(split_line[1][0])
            elif split_line[0] == "Starting":
                items = [int(item.strip(",")) for item in split_line[2:]]
            elif split_line[0] == "Operation:":
                if "+" in split_line:
                    operation = ("+", int(split_line[-1]))
                elif "*" in split_line:
                    if "old" == split_line[-1]:
                        operation = ("**", 2)
                    else:
                        operation = ("*", int(split_line[-1]))
            elif split_line[0] == "Test:":
                div_test_by = int(split_line[-1])
            elif split_line[1] == "true:":
                div_true_monkey_id = int(split_line[-1])
            elif split_line[1] == "false:":
                div_false_monkey_id = int(split_line[-1])
                monkey = Monkey(monkey_id, items, operation, div_test_by, div_true_monkey_id, div_false_monkey_id)
                self.monkeys.append(monkey)
            else:
                raise (ValueError(f"Cannot read monkey input line: {line}!"))

    def play_rounds(self, num_rounds=20, relieve=True):
        if not relieve:
            lcm_modulus = lcm(*[monkey.div_test_by for monkey in self.monkeys])
        for _ in range(num_rounds):
            for monkey in self.monkeys:
                if relieve:
                    monkey.inspect()
                    monkey.relieve()
                else:
                    monkey.inspect(lcm_modulus)
                thrown_items = monkey.throw_items()
                for monkey_id, items in thrown_items.items():
                    self.monkeys[monkey_id].items.extend(reversed(items))

    def get_monkey_business_level(self):
        top_two_inspects = sorted([monkey.inspected_num for monkey in self.monkeys], reverse=True)[:2]
        return top_two_inspects[0] * top_two_inspects[1]


def main():
    monkey_game = MonkeyInTheMiddle()
    monkey_game.read_monkeys()
    another_monkey_game = deepcopy(monkey_game)
    monkey_game.play_rounds()
    monkey_business_level = monkey_game.get_monkey_business_level()
    another_monkey_game.play_rounds(num_rounds=10000, relieve=False)
    not_relieved_monkey_business_level = another_monkey_game.get_monkey_business_level()
    utils.write_answers_to_file(monkey_business_level, not_relieved_monkey_business_level, file_name="answer_11.txt")
    print(monkey_business_level, not_relieved_monkey_business_level)


if __name__ == "__main__":
    main()
