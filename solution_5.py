STACK_WIDTH = 3
STACK_GAP = 1
CRATE_START = "["
NUM_BOXES_INDEX = 1
TAKING_STACK_INDEX = 3
RECEIVING_STACK_INDEX = 5
INPUT_PATH = "inputs/input_5.txt"

from utils import utils


def get_stack_number(crate_start_pos: int) -> int:
    return crate_start_pos // (STACK_WIDTH + STACK_GAP) + 1


def parse_stacks_row(line: str) -> dict:
    stacks_elements = dict()
    for pos, element in enumerate(line):
        if element == CRATE_START:
            stacks_elements[get_stack_number(pos)] = line[pos + 1]
    return stacks_elements


def read_stacks(input_path: str = INPUT_PATH) -> dict:
    stacks = dict()
    with open(input_path, "r") as input_data:
        for line in input_data:
            if line == "\n":
                return stacks
            stacks_row = parse_stacks_row(line)
            for stack_id, element in stacks_row.items():
                if stack_id in stacks:
                    # insert is O(n), could just append and then work with reversed stacks
                    stacks[stack_id].insert(0, element)
                else:
                    stacks[stack_id] = [element]


def parse_procedure_step(line: str) -> tuple:
    split_line = line.split()
    return int(split_line[NUM_BOXES_INDEX]), int(split_line[TAKING_STACK_INDEX]), int(split_line[RECEIVING_STACK_INDEX])


def read_procedure(input_path=INPUT_PATH) -> list:
    procedure = list()
    with open(input_path, "r") as input_data:
        for line in input_data:
            if line[:4] == "move":
                procedure.append(parse_procedure_step(line))
    return procedure


def execute_procedure(stacks, procedure, old_model=True):
    for step in procedure:
        num_boxes = step[0]
        taking_stack_id = step[1]
        receiving_stack_id = step[2]
        if old_model:
            for _ in range(num_boxes):
                stacks[receiving_stack_id].append(stacks[taking_stack_id].pop())
        else:
            stacks[receiving_stack_id].extend(stacks[taking_stack_id][-num_boxes:])
            stacks[taking_stack_id] = stacks[taking_stack_id][:-num_boxes]
    return stacks


def get_top_crates_names(stacks):
    top_crates_names = ""
    for i in range(len(stacks.keys())):
        top_crates_names += stacks[i + 1][-1]
    return top_crates_names


def main():
    stacks = read_stacks()
    procedure = read_procedure()
    old_stacks = execute_procedure(stacks, procedure)
    stacks = read_stacks()  # have to reload as stacks.copy() doesn't make a copy of the lists inside
    new_stacks = execute_procedure(stacks, procedure, old_model=False)
    old_top_crates_names = get_top_crates_names(old_stacks)
    new_top_crates_names = get_top_crates_names(new_stacks)
    utils.write_answers_to_file(old_top_crates_names, new_top_crates_names, file_name="answer_5.txt")
    print(old_top_crates_names, new_top_crates_names)


if __name__ == "__main__":
    main()
